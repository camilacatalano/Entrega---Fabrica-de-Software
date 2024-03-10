from rest_framework.viewsets import ModelViewSet
from rest_framework.views import Response, status
from .serializers import CadastroClienteSerializer
from ..models import CadastroCliente
import requests

class CadastroClienteViewSet(ModelViewSet):
    queryset = CadastroCliente.objects.all ()
    serializer_class = CadastroClienteSerializer

    def create(self, request, *args, **kwargs):

        response = requests.get(f"https://api.genderize.io?name={request.data.get('name')}")
        print(f"Resposta da API externa: {response.json()}")

        genero = response.json().get("gender")
        print(f"Genero:{genero}")

        serializer = CadastroClienteSerializer(data={**request.data,"genero":genero})
        serializer.is_valid(raise_exception=True)
        serializer.save

        return Response(serializer.validated_data, status.HTTP_201_CREATED)
        

