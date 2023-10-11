# Classificação de frases por setor

O projeto está dividido em 3 partes:
- Modelo (de aprendizado de máquina, no diretório webAPI/django_app/model)
- Front-end (com React, no diretório js_interface)
- Back-end (com Django / Django REST Framework, no diretório webAPI)

## Instalando

### Front-end
O projeto React pode ser instalado da maneira padrão, dentro da pasta:

`npm install`

Que instalará as dependências padrões e mais as utilizadas: boostrap, react-bootstrap e axios

### Back-end
Já o projeto Django tem apenas as suas bibliotecas como dependências, podendo ser instalado com o gerenciador de pacotes pip:
- django
- djangorestframework
- django-cors-headers

### Modelo
Inclui as seguintes bibliotecas:
- pandas
- sklearn
- skmultilearn
- nltk
Sendo que a nltk é necessário instalar as dependências adicionais (dentro do ambiente de execução python):

`import nltk`

`nltk.download('rslp')`

## Utilizando

É possível utilizar apenas o modelo de aprendizado de máquina e ver seu resultado (com f1-score) executando diretamente o arquivo "webAPI/django_app/model/evaluation.py". Para utilizar a aplicação completa, é necessário inicializar o servidor django
`python manage.py runserver`
e invocar a url "/train" (exemplo: http://127.0.0.1/train) que irá convocar uma view para realizar o treinamento do modelo e salvar o resultado em disco

Para utilizar a predição, é possível iniciar o serviço react:
`npm start`
preencher o formulário e submeter
