Mindsounds é um pequeno clone de Twitter desenvolvido com Django para a disciplina INF1407 (Programação para Web) da PUC-Rio.

## Pré-requisitos

- Python 3.12 ou superior
- Django 5.1 ou superior

Pré-requisitos inferiores podem funcionar, mas não foram testados.

## Testando localmente

Primeiramente, entre no diretório do projeto. Na primeira execução, é necessário criar o banco de dados:

```bash
python manage.py migrate
```

Uma vez que o banco de dados foi criado, você pode rodar o servidor de desenvolvimento:

```bash
python manage.py runserver
```

## Gerando container Docker

Para gerar um container Docker, é necessário ter o Docker instalado. Com o Docker instalado, basta rodar o seguinte comando:

```bash
docker build -t mindsounds .
```
