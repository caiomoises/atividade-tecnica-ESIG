import os
import openai
import psycopg2
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.pgvector import PGVector
from flask import Flask, request, jsonify
from rest_framework import viewsets
from ..models import Documento, Conversa, Mensagem
from ..serializers import DocumentoSerializer, ConversaSerializer, MensagemSerializer

# Configurações
openai.api_key = os.getenv("OPENAI_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

def create_app():
    app = Flask(__name__)

    @app.route("/upload", methods=["POST"])
    def upload_file():
        file = request.files.get("file")
        if not file:
            return jsonify({"error": "Nenhum arquivo enviado"}), 400
        
        # TODO: Processar arquivo e armazenar embeddings no PostgreSQL
        return jsonify({"message": "Arquivo processado com sucesso"})

    @app.route("/ask", methods=["POST"])
    def ask_question():
        data = request.get_json()
        question = data.get("question")
        
        if not question:
            return jsonify({"error": "Pergunta não fornecida"}), 400
        
        # TODO: Recuperar contexto usando RAG e enviar para OpenAI
        response = {"answer": "Resposta gerada pelo ChatBot"}
        return jsonify(response)

    return app

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

class ConversaViewSet(viewsets.ModelViewSet):
    queryset = Conversa.objects.all()
    serializer_class = ConversaSerializer

class MensagemViewSet(viewsets.ModelViewSet):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
