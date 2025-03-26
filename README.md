<h1 align="center">ATIVIDADE TECNICA ESIG GROUP 🤖💡</h1>

# Instruções para executar o projeto

## Configurações iniciais:
Certifique-se de que você tem o Python instalado em sua máquina. Caso não tenha, você pode baixá-lo [Aqui](https://www.python.org/downloads/.)

## Crie um ambiente virtual (opcional, porém, recomendo)

Uma boa prática de programação é criar um ambiente virtual com o intuito de isolar as dependências do seu projeto. 

Para criar um ambiente virtual use o seguinte comando: 

    python3 -m venv nome-do-ambiente

Após ter criado o ambiente, é necessario ativa-lo usando o comando:

- No Windows:

        nome-do-ambiente\Scripts\activate

- No macOS e Linux:

        source nome-do-ambiente/bin/activate

Com o ambiente virtual ativo, precisamos instalar o Django e o Djangorestframework usando o pip (gerenciador de pacotes do python)

    pip install django djangorestframework

Após a instalação do Django, vamos criar um projeto:

    django-admin startproject nome-do-projeto .

Crie um app Django:

    python manage.py startapp nome-do-app

Execute as migrações:

    python manage.py migrate
            ou
    python manege.py makemigrations

Execute o servidor:

    python manege.py runserver

Agora você pode acessar sua API em "http://127.0.0.1:8000/".  

# Criando e alterando a senha de um super usuário Django
    Criando:
        python manage.py createsuperuser
    Editando:
        python manage.py changepassword USERNAME
