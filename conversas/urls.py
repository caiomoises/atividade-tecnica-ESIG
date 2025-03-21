from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include
from .views import(
    CustomTokenObtainPairView,
    DocumentoViewSet,
    ConversaViewSet,
    MensagemViewSet,

)

router = DefaultRouter()


router.register(r'documentos', DocumentoViewSet)
router.register(r'conversas', ConversaViewSet)
router.register(r'mensagens', MensagemViewSet)

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
]