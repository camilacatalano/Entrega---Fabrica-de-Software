## Criar uma API Necessário: models; viewsets; serializers; urls, admin; 

## Crio uma pasta chamada API dentro do nome do app que vou criar, e dentro da API crio o viewsets, serializers, e urls. 
## Serializers: Filtra/Trata os dados Viewsets: Funcionalidades da API, exemplo: "create", passa os dados do models e encaminha para tabela Urls: Aponto o caminho das rotas dos dados No insomnia faremos o teste da rota, a funcionalidade, como um protótico, ele faz as requisições da APi 
## Admin: Registra a parte de admin na API Insomnia: GET >>> http://+caminho do django/API/ NO TERMINAL:::: (Crtl+J) -Chamo a venv (ambiente virtual) python -m venv "nome da pasta" -Ativar o ambiente ven: .\venv (nome da pasta)\Scripts\activate.ps1 -Instalo as bibliotecas (Django e RestFramework) "pip install django djangorestframework" -Crio a pasta com o projeto jango.admin startproject "nome do projeto" + o ponto no final -Criar o app: django.admin startproject "+nome do projeto E O PONTO FINAL -
## Criar o superusuario (Posso fazer em qualquer etapa da criação do projeto) python manage.py createsuperuser (ele pode as informações)

## Vou na pasta do projeto e abro o settings.py, procuro o dicionário chamado Installed Apps e adiciono 'rest_framework' 'nome do seu app',

## python manage.py migrate >>> Para dar as migrações (sobe para o banco de dados) -python manage.py makemigrations >>> salvar as migrações (cria o SQL/exporta os dados) -python manage.py runserver >>> Dá run na API

## Vou em Models e crio minha classe e entrada de dados ex: from django.db import models

	 class Cadastro(models.Model):
	 nome = models.CharField(max_length=20)
	 último_nome = models.CharField(max_length=40)
	 telefone = models.CharField(max_length=35)
	 genero = models.CharField(max_length=10)

## Insiro o URL com a porta no Insomnia como HTTPS new request, e utilizo os operadores