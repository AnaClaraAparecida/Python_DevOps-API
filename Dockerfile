#1: preparar distro + instalação do python
FROM python:3

#2: instalar as dependencias a nivel da aplicaçao (pip)
COPY ./requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt 

#3 copiar a aplicaçao para o contexto da imagem 
RUN mkdir /app

COPY ./app/

WORKDIR /app

#4 configurar a porta de conexao da app (5000)
EXPOSE 5000

ENV FLASK_ENV=development

#5 executar um comando para subir o server flask 
CMD flask run -h '0.0.0.0'
 
