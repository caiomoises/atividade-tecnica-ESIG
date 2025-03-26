from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include
from .views import(
    CustomTokenObtainPairView,
    DocumentoViewSet,
    ConversaViewSet,
    MensagemViewSet,
    PerguntaViewSet,
    ChatView,
)

router = DefaultRouter()


router.register(
    r'documentos',
    DocumentoViewSet,
    basename="documentos"
)
router.register(
    r'conversas',
    ConversaViewSet,
    basename="conversas"
)
router.register(
    r'mensagens',
    MensagemViewSet,
    basename="mensagens"
)
router.register(
    r'perguntas',
    PerguntaViewSet,
    basename="perguntas"
)

urlpatterns = [
    path(
        'login/',
        CustomTokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        '',
        include(router.urls)
    ),
    path('chat/', ChatView.as_view(), name='chat'),
]