from rest_framework.serializers import ModelSerializer
from ..models import CadastroCliente

class CadastroClienteSerializer(ModelSerializer):
    class Meta:
        model = CadastroCliente
        fields = ["nome","idade","email","genero"]
