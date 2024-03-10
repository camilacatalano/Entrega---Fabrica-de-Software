from django.db import models

# Create your models here.
class CadastroCliente(models.Model):
    nome = models.CharField(verbose_name="Nome do usuário",max_length=50)
    idade = models.IntegerField(verbose_name = "Idade do usuário")
    email = models.EmailField(verbose_name = "Email do usuário")
    genero = models.CharField(verbose_name = "Gênero do usuário",max_length=20)

    def __str__(self) -> str:
        return f'{self.nome}'
