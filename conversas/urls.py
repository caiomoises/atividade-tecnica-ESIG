from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include
from .views import(
    CustomTokenObtainPairView
)

router = DefaultRouter()

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