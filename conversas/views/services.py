import os
import tempfile
from pypdf import PdfReader
from docx import Document
from ..models.vetorRAG import VetorDocumento
from ..models import Conversa, Mensagem
from django.utils import timezone
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import PGVector
from langchain.schema import Document
from decouple import config
import logging
import openai
from pgvector.django import L2Distance

logger = logging.getLogger(__name__)

def extrair_texto(arquivo):
    """Extrai texto de um arquivo PDF ou DOCX"""
    ext = os.path.splitext(arquivo.name)[-1].lower()
    texto = ""

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(arquivo.read())
        temp_file_path = temp_file.name

    if ext == ".pdf":
        reader = PdfReader(temp_file_path)
        for page in reader.pages:
            texto += page.extract_text() + "\n"

    elif ext == ".docx":
        doc = Document(temp_file_path)
        for para in doc.paragraphs:
            texto += para.text + "\n"

    os.remove(temp_file_path)
    return texto

def gerar_e_salvar_embedding(texto, documento):
    """Gera embeddings do texto e armazena no PostgreSQL"""
    try:
        openai_api_key = config("OPENAI_API_KEY")
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        embedding = embeddings.embed_documents([texto])[0]

        doc = Document(
            page_content=texto,
            metadata={
                "documento_id": documento.id,
                "documento_nome": documento.nome,
            }
        )

        vetor = VetorDocumento(
            page_content=texto,
            documento=documento,
            embedding=embedding,
            metadata=doc.metadata
        )
        vetor.save()

    except Exception as e:
        logger.error(f"Erro ao gerar e salvar embedding: {e}")

def buscar_contexto(pergunta, usuario=None, conversa_id=None):
    """Busca contexto e salva a conversa no banco de dados"""
    try:
        openai_api_key = config("OPENAI_API_KEY")
        config_banco = config("DATABASE_URL")
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        openai.api_key = openai_api_key

        if conversa_id:
            conversa = Conversa.objects.get(id=conversa_id)
        else:
            conversa = Conversa.objects.create(
                usuario=usuario.username if usuario else "Anônimo",
                criado_em=timezone.now()
            )

        mensagem = Mensagem.objects.create(
            conversa=conversa,
            texto=pergunta
        )

        pergunta_embedding = embeddings.embed_documents([pergunta])[0]
        store = VetorDocumento.objects.order_by(
            L2Distance('embedding', pergunta_embedding)
        ).last()

        if store is not None:
            mensagem_filtrada = Mensagem.objects.filter(
                conversa=conversa,
                texto=store.documento,
                resposta=store.page_content
            ).exists()
            if not mensagem_filtrada:
                mensagem_extra = Mensagem.objects.create(
                    conversa=conversa,
                    texto=store.documento,
                    resposta=store.page_content,
                )
        
        resposta = enviar_mensagem(pergunta, obter_historico(conversa))
        

        mensagem.resposta = resposta
        mensagem.save()

        return {
            "resposta": resposta,
            "conversa_id": conversa.id
        }

    except Exception as e:
        logger.error(f"Erro ao buscar contexto: {e}")
        return {
            "resposta": "Desculpe, ocorreu um erro ao processar sua solicitação.",
            "conversa_id": conversa.id if 'conversa' in locals() else None
        }

def obter_historico(conversa):
    """Retorna o histórico de mensagens no formato do OpenAI"""
    mensagens = conversa.mensagens.all().order_by('criado_em')
    historico = []
    
    for msg in mensagens:
        historico.append({"role": "user", "content": msg.texto})
        if msg.resposta:
            historico.append({"role": "assistant", "content": msg.resposta})
    
    return historico

def enviar_mensagem(pergunta, contexto="", historico=None):
    """Envia mensagem ao OpenAI com contexto e histórico"""
    try:
        messages = []
        
        if contexto:
            messages.append({
                "role": "system",
                "content": f"Use estas informações como contexto: {contexto}"
            })
        
        if historico:
            messages.extend(historico)
        
        messages.append({"role": "user", "content": pergunta})

        resposta = openai.chat.completions.create(
            model="gpt-4-turbo",
            messages=messages,
            temperature=0.7
        )

        return resposta.choices[0].message.content

    except Exception as e:
        logger.error(f"Erro ao enviar mensagem: {e}")
        return "Desculpe, ocorreu um erro ao processar sua mensagem."