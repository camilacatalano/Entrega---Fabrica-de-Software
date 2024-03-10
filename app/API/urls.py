from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .viewsets import CadastroClienteViewSet

router = DefaultRouter()
router.register('cadastro', CadastroClienteViewSet)

urlpatterns = [
  path('api/',include(router.urls))
]