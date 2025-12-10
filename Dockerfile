# Multi Stage Building 

## Build #1 
#1.1: preparar distro + instalação do python
FROM python:3.6-alpine as base

#2: instalar as dependencias a nivel da aplicaçao (pip)
COPY ./requirements.txt /tmp

RUN mkdir /install 

RUN pip install --prefix=/intall -r  /tmp/requirements.txt 

## Build #2

FROM base

##2.1 copiar as dependencias ja preparadas 

COPY --from=base /install /usr/local 

#2.2 copiar a aplicaçao para o contexto da imagem 
RUN mkdir /app

COPY ./app/

WORKDIR /app

#2.3 configurar a porta de conexao da app (5000)
EXPOSE 5000

#2.4 definir variaveis de ambiente 
ENV FLASK_ENV=development

#5 executar um comando para subir o server flask 
CMD flask run -h '0.0.0.0'
 
