# fazendo o pull da imagem oficial no Docker Hub
FROM python:3.10

# setando variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copiando os requisitos necessários para a aplicação rodar
COPY ./requirements.txt .

# executando a instalação dos pacotes
RUN pip install -r requirements.txt

# definindo o diretório de trabalho no contêiner
WORKDIR /code

# copiando todos os arquivos para o diretório de trabalho
COPY . /code/