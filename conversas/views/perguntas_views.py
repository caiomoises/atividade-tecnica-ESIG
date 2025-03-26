from openai import OpenAI
from .services import buscar_contexto
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import AnonymousUser

class PerguntaViewSet(viewsets.ViewSet):
    def create(self, request):
        pergunta = request.data.get("pergunta")
        if not pergunta:
            return Response({"error": "Pergunta não fornecida"}, status=400)
        
        usuario = request.user if not isinstance(request.user, AnonymousUser) else None
        conversa_id = request.data.get("conversa_id")
        
        resultado = buscar_contexto(
            pergunta=pergunta,
            usuario=usuario,
            conversa_id=conversa_id
        )
        
        return Response(resultado)

        # resposta = OpenAI().chat.completions.create(
        #     model="gpt-4-turbo",
        #     messages=[{"role": "system", "content": "Responda apenas com base nos documentos."},
        #               {"role": "user", "content": contexto + "\n\n" + pergunta}]
        # )["choices"][0]["message"]["content"]

        # return Response({"resposta": resposta})
