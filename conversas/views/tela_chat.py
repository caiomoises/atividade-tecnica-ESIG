from django.shortcuts import render
from rest_framework.views import APIView

class ChatView(APIView):
    def get(self, request):
        return render(request, 'index.html')