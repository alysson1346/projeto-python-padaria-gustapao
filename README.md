# Documentação da API

## Tabela de Conteúdos

- [Visão Geral](#1-visão-geral)
  - [Diagrama Entidade Relacionamento](#11-diagrama-entidade-relacionamento)
  - [Tecnologias Usadas](#12-tecnologias-usadas)
- [Início Rápido](#2-início-rápido)
  - [Instalando Dependências](#21-instalando-dependências)
  - [Server](#22-server)
- [Endpoints](#3-endpoints)
- [Equipe](#4-equipe)

---

## 1. Visão Geral

Este projeto visa ajudar uma panificadora localizada em Curitiba, Brasil, que possui um excelente atendimento e produtos, porém, não possui um sistema dedicado ao gerenciamento de pedidos. Para resolver o problema foi desenvolvido uma API onde seria possível realizar o cadastro de usuários e produtos como também solicitar uma encomenda.

---

### 1.1. Diagrama Entidade Relacionamento

[ Voltar para o topo ](#tabela-de-conteúdos)

![](/assets/img/diagrama-gustapao.jpg)

---

---

### 1.2. Tecnologias Usadas

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Heroku](https://www.heroku.com/)

---

## 2. Início Rápido

[ Voltar para o topo ](#tabela-de-conteúdos)

### 2.1. Instalando Dependências

Crie o ambiente virtual com o comando:

```shell
python -m venv venv
```

Ative o venv com o comando:

Linux:

```shell
source venv/bin/activate
```

Windows:

```shell
source venv/Scripts/activate
```

Instale as dependências com o comando:

```shell
pip install -r requirements.txt
```

Em seguida, crie um arquivo **.env**, copiando o formato do arquivo **.env.example**:

```
cp .env.example .env
```

Configure suas variáveis de ambiente com suas credenciais do Postgres e uma nova database da sua escolha.

Execute as migrações:

```shell
python ./manage.py migrate
```

Crie um superuser com o comando e preencha as informações solicitadas:

```shell
python ./manage.py createsuperuser
```

### 2.2. Server

Execute o comando para rodar o servidor na máquina local na porta 8000:

```
python ./manage.py runserver
```

---

## 3. Endpoints

[ Voltar para o topo ](#tabela-de-conteúdos)

### Índice

- [Accounts](#1-accounts)

  - [Criação usuário comum](#11-criação-usuário-comum)
  - [Criação de Funcionário](#12-criação-de-funcionário)
  - [Listando todos usuários](#13-listando-todos-usuários)
  - [login usuário](#14-login-usuário)
  - [Listando usuário por id](#15-listando-usuário-por-id)
  - [Atualizar usuário por id](#16-atualizar-usuário-por-id)
  - [Desativar ou ativar usuário](#17-desativar-ou-ativar-usuário)
  - [Atualizar permissões usuário](#18-atualizar-permissões-usuário)

- [Categories](#2-categories)

  - [Criar categoria](#21-criar-categoria)
  - [Listar categorias](#22-listar-categorias)
  - [Atualizar categorias](#23-atualizar-categorias)
  - [Deletar categorias](#24-deletar-categorias)

- [Ingredients](#3-ingredients)

  - [Criar ingrediente](#31-criar-ingrediente)
  - [Listar ingredientes](#32-listar-ingredientes)
  - [Atualizar ingrediente](#33-atualizar-ingrediente)
  - [Deletar ingrediente](#34-deletar-ingrediente)

- [Orders](#4-orders)
  - [Criar order](#41-criar-order)
  - [Listar todos os orders](#42-listar-todos-os-orders)
  - [Listar orders do própio user](#43-listar-orders-do-própio-user)
  - [Listar orders por data](#44-listar-orders-por-data)
  - [Atualizar orders](#45-atualizar-orders)
  - [Atualizar status orders](#46-atualizar-status-orders)
  - [Deletar order](#47-deletar-order)

---

## 1. **Accounts**

[ Voltar para os Endpoints ](#3-endpoints)

O objeto User é definido como:

| Campo        | Tipo    | Descrição                                                     |
| ------------ | ------- | ------------------------------------------------------------- |
| id           | string  | Identificador único do usuário                                |
| is_superuser | boolean | Valor Booleano que identifica se o usuário é um super usuário |
| is_staff     | boolean | Valor Booleano que identifica se o usuário é um funcionário   |
| is_active    | boolean | Valor Booleano que identifica se o usuário está ativo         |
| date_joined  | date    | Nos mostra quando foi criado o usuário.                       |
| username     | string  | O nome do usuário.                                            |
| email        | string  | O e-mail do usuário.                                          |
| first_name   | string  | Primeiro nome do usuário.                                     |
| last_name    | string  | Último nome do usuário.                                       |
| password     | string  | A senha de acesso do usuário                                  |
| cellphone    | string  | Telefone de contato do usuário                                |

---

### 1.1. **Criação usuário comum**

### `/api/accounts/`

### Exemplo de Request:

```
POST /api/accounts/
Host: http://localhost:8000/api/accounts/
Authorization: None
Content-type: application/json
```

### Corpo da Requisição:

```json
{
  "username": "Kennedy",
  "email": "kennedy@mail.com",
  "password": "1234",
  "first_name": "Kennedy",
  "last_name": "Client",
  "cellphone": "019999999991"
}
```

### Exemplo de Response:

```
201 Created
```

```json
{
  "id": "2a95db4f-a7e7-4696-8058-c2b0a9b20177",
  "date_joined": "2022-10-10T19:38:26.116851Z",
  "username": "Kennedy",
  "email": "kennedy@mail.com",
  "first_name": "Kennedy",
  "last_name": "Client",
  "cellphone": "019999999991"
}
```

### Possíveis Erros:

| Código do Erro  | Descrição                                                                              |
| --------------- | -------------------------------------------------------------------------------------- |
| 400 Bad Request | Se username, email ou cellphone já existirem retornará um JSON como no exemplo abaixo. |

```json
{
  "username": ["account with this username already exists."],
  "email": ["account with this email already exists."],
  "cellphone": ["account with this cellphone already exists."]
}
```

[ Voltar para os Endpoints ](#3-endpoints)

---

### 1.2. **Criação de Funcionário**

### `/api/accounts/employee/`

Obs: Necessário estar logado como superuser

### Exemplo de Request:

```
POST /api/accounts/employee/
Host: http://localhost:8000/api/accounts/employee/
Authorization: Token {token}
Content-type: application/json
```

### Corpo da Requisição:

```json
{
  "username": "Regis",
  "email": "regis@mail.com",
  "password": "1234",
  "first_name": "regis",
  "last_name": "employee",
  "cellphone": "019154789652"
}
```

### Exemplo de Response:

```
201 Created
```

```json
{
  "id": "55140c67-158b-47fb-a955-26c4e0b82955",
  "is_superuser": false,
  "is_staff": true,
  "is_active": true,
  "date_joined": "2022-10-10T19:38:36.965794Z",
  "username": "Regis",
  "email": "regis@mail.com",
  "first_name": "regis",
  "last_name": "employee",
  "cellphone": "019154789652"
}
```

### Possíveis Erros:

| Código do Erro  | Descrição                                                                              |
| --------------- | -------------------------------------------------------------------------------------- |
| 403 Forbidden   | Erro retornado caso o usuário não tenha a permissão necessária.                        |
| 400 Bad Request | Se username, email ou cellphone já existirem retornará um JSON como no exemplo abaixo. |

```json
{
  "username": ["account with this username already exists."],
  "email": ["account with this email already exists."],
  "cellphone": ["account with this cellphone already exists."]
}
```

[ Voltar para os Endpoints ](#3-endpoints)

---

### 1.3. **Listando todos usuários**

[ Voltar aos Endpoints ](#3-endpoints)

### `/api/accounts/`

Obs: Necessário estar logado como Superuser para ter acesso a rota

### Exemplo de Request:

```
GET /api/accounts/
Host: http://localhost:8000/api/accounts/
Authorization: Token {token}
```

### Corpo da Requisição:

```json
Vazio
```

### Exemplo de Response:

```
200 OK
```

```json
{
  "count": 6,
  "next": "http://localhost:8000/api/accounts/?page=2",
  "previous": null,
  "results": [
    {
      "id": "f4d6e6a9-7246-4a89-ae25-d1457df170c7",
      "is_superuser": false,
      "is_staff": true,
      "is_active": true,
      "date_joined": "2022-10-10T19:38:40.671405Z",
      "username": "Lucira",
      "email": "lucira@mail.com",
      "first_name": "lucira",
      "last_name": "employee",
      "cellphone": "019775467772"
    },
    {
      "id": "88589982-84b1-4bff-b55d-8920a082bfc7",
      "is_superuser": false,
      "is_staff": false,
      "is_active": true,
      "date_joined": "2022-10-10T19:38:29.048500Z",
      "username": "Joao",
      "email": "joao@mail.com",
      "first_name": "Joao",
      "last_name": "client",
      "cellphone": "01988888882"
    },
    {
      "id": "55140c67-158b-47fb-a955-26c4e0b82955",
      "is_superuser": false,
      "is_staff": true,
      "is_active": true,
      "date_joined": "2022-10-10T19:38:36.965794Z",
      "username": "Regis",
      "email": "regis@mail.com",
      "first_name": "regis",
      "last_name": "employee",
      "cellphone": "019154789652"
    },
    {
      "id": "2a95db4f-a7e7-4696-8058-c2b0a9b20177",
      "is_superuser": false,
      "is_staff": false,
      "is_active": true,
      "date_joined": "2022-10-10T19:38:26.116851Z",
      "username": "Kennedy",
      "email": "kennedy@mail.com",
      "first_name": "Kennedy",
      "last_name": "Client",
      "cellphone": "019999999991"
    },
    {
      "id": "28bd5a11-e26e-41b2-a6ee-a4d43bf49de9",
      "is_superuser": false,
      "is_staff": false,
      "is_active": true,
      "date_joined": "2022-10-10T19:38:32.492489Z",
      "username": "Paulo77",
      "email": "paulo778@mail.com",
      "first_name": "paulo",
      "last_name": "client",
      "cellphone": "017778778772"
    }
  ]
}
```

### Possíveis Erros:

Nenhum, o máximo que pode acontecer é retornar uma lista vazia.

---

### 1.4. **login usuário**

### `/accounts/login`

### Exemplo de Request:

```
POST /accounts/login/
Host: http://localhost:8000/api/accounts/login/
Authorization: None
Content-type: application/json

```

Obs: Login pode ser realizado com email, username ou cellphone

### Corpo da Requisição:

```json
{
  "email": "regis@mail.com",
  "password": "1234"
}
```

### Exemplo de Response:

```
201 Created
```

```json
{
  "token": "9e6f2e4ca5c4be83a0a647e3cb9fba75ab35e9a7"
}
```

[ Voltar aos Endpoints ](#3-endpoints)

---

### 1.5. **listando usuário por id**

### `/accounts/{id}`

Obs: Somente Admin ou o própio usuário terá acesso as informações dessa rota

### Exemplo de Request:

```
GET /accounts/{id}
Host: http://localhost:8000/api/accounts/{id}/
Authorization: Bearer {token}
```

### Corpo da Requisição:

```json
Vazio
```

### Exemplo de Response:

```
200 OK
```

```json
{
  "id": "55140c67-158b-47fb-a955-26c4e0b82955",
  "is_superuser": false,
  "is_staff": true,
  "is_active": true,
  "date_joined": "2022-10-10T19:38:36.965794Z",
  "username": "Regis",
  "email": "regis@mail.com",
  "first_name": "regis",
  "last_name": "employee",
  "cellphone": "019154789652"
}
```

### Possíveis Erros:

| Código do Erro   | Descrição                                        |
| ---------------- | ------------------------------------------------ |
| 401 Unauthorized | invalid Token.                                   |
| 403 Forbidden    | Usuário não tem acesso ou permissão para a rota. |
| 404 Not Found    | id passado como parâmetro não existe             |

[ Voltar aos Endpoints ](#3-endpoints)

---

### 1.6. **Atualizar usuário por id**

### `/accounts/{id}`

Obs: Somente Admin ou o própio usuário terá acesso as informações dessa rota

### Exemplo de Request:

```
PATCH /accounts/{id}
Host: http://localhost:8000/api/accounts/{id}/
Authorization: Bearer {token}
```

Obs: Somente superuser ou o própio usuário têm autorização nessa rota

### Corpo da Requisição:

No corpo da requisição você pode passar somente a informação que você quer alterar

```json
{
  "last_name": "Patch"
}
```

### Exemplo de Response:

```
200 OK
```

Somente o dado passado na requisição foi atualizado:

```json
{
  "date_joined": "2022-10-10T19:38:36.965794Z",
  "username": "Regis",
  "email": "regis@mail.com",
  "first_name": "regis",
  "last_name": "Patch",
  "cellphone": "019154789652"
}
```

### Possíveis Erros:

| Código do Erro   | Descrição                                        |
| ---------------- | ------------------------------------------------ |
| 401 Unauthorized | invalid Token.                                   |
| 403 Forbidden    | Usuário não tem acesso ou permissão para a rota. |
| 404 Not Found    | id passado como parâmetro não existe             |

[ Voltar aos Endpoints ](#3-endpoints)

---

### 1.7. **Desativar ou ativar usuário**

### `/accounts/{id}/management/`

Obs: Somente Admin terá permissão na rota.

### Exemplo de Request:

```
PATCH /accounts/{id}/management/
Host: http://localhost:8000/api/accounts/{id}/management/
Authorization: Bearer {token}
```

Obs: Somente superuser ou o própio usuário têm autorização nessa rota

### Corpo da Requisição:

No corpo da requisição você pode passar somente a informação que você quer alterar

```json
{
  "is_active": false
}
```

### Exemplo de Response:

```
200 OK
```

Somente o dado passado na requisição foi atualizado:

```json
{
  "id": "55140c67-158b-47fb-a955-26c4e0b82955",
  "username": "Regis",
  "is_active": false
}
```

### Possíveis Erros:

| Código do Erro   | Descrição                                        |
| ---------------- | ------------------------------------------------ |
| 401 Unauthorized | invalid Token.                                   |
| 403 Forbidden    | Usuário não tem acesso ou permissão para a rota. |
| 404 Not Found    | id passado como parâmetro não existe             |

[ Voltar aos Endpoints ](#3-endpoints)

---

### 1.8. **Atualizar permissões usuário**

### `/accounts/{id}/update-permissions/`

Obs: Somente Admin terá permissão na rota.

### Exemplo de Request:

```
PATCH /accounts/{id}/update-permissions/
Host: http://localhost:8000/api/accounts/{id}/update-permissions/{
	"is_superuser": true,
	"is_staff": false
}
Authorization: Bearer {token}
```

Obs: Somente superuser ou o própio usuário têm autorização nessa rota

### Corpo da Requisição:

No corpo da requisição você pode passar somente a informação que você quer alterar

```json
{
  "is_superuser": true,
  "is_staff": false
}
```

### Exemplo de Response:

```
200 OK
```

```json
{
  "is_superuser": true,
  "is_staff": false
}
```

### Possíveis Erros:

| Código do Erro   | Descrição                                        |
| ---------------- | ------------------------------------------------ |
| 401 Unauthorized | invalid Token.                                   |
| 403 Forbidden    | Usuário não tem acesso ou permissão para a rota. |
| 404 Not Found    | id passado como parâmetro não existe             |

[ Voltar aos Endpoints ](#3-endpoints)

---

## 2. **Categories**

[ Voltar para os Endpoints ](#3-endpoints)

O objeto User é definido como:

| Campo | Tipo   | Descrição                      |
| ----- | ------ | ------------------------------ |
| id    | string | Identificador único do usuário |
| name  | string | Nome da categoria              |

---

### 2.1. **Criar categoria**

### `/api/products/section/categories/`

Obs: Somente superuser ou staff têm permissão.

### Exemplo de Request:

```
POST api/products/section/categories/
Host: http://localhost:8000/api/products/section/categories/
Authorization: Token {token}
Content-type: application/json
```

### Corpo da Requisição:

```json
{
  "name": "salgados"
}
```

### Exemplo de Response:

```
201 Created
```

```json
{
  "id": "9cc37f69-942e-4d84-a437-e26c6c49ce33",
  "name": "salgados"
}
```

### Possíveis Erros:

| Código do Erro | Descrição                  |
| -------------- | -------------------------- |
| 403 Forbidden  | Usuário não tem permissão. |

[ Voltar para os Endpoints ](#3-endpoints)

---

### 2.2. **Listar categorias**

### `/api/products/section/categories/`

### Exemplo de Request:

```
GET api/products/section/categories/
Host: http://localhost:8000/api/products/section/categories/
Authorization: None
Content-type: application/json
```

### Corpo da Requisição:

```json
{}
```

### Exemplo de Response:

```
200 OK
```

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "acf47f06-6bca-469e-ac21-b79f93a78df5",
      "name": "salgados"
    },
    {
      "id": "2f6932fb-7b30-4f44-9647-d3bbeb5f1a2d",
      "name": "doce"
    }
  ]
}
```

[ Voltar para os Endpoints ](#3-endpoints)

---

---

### 2.3. **Atualizar categorias**

### `/api/products/section/categories/`

### Exemplo de Request:

Obs: Somente superuser ou staff tem permissão

```
PATCH api/products/section/categories/{id}/
Host: http://localhost:8000/api/products/section/categories/{id}/
Authorization: Token {token}
Content-type: application/json
```

### Corpo da Requisição:

```json
{
  "name": "Salgadinhos"
}
```

### Exemplo de Response:

```
200 OK
```

```json
{
  "id": "acf47f06-6bca-469e-ac21-b79f93a78df5",
  "name": "Salgadinhos"
}
```

[ Voltar para os Endpoints ](#3-endpoints)

---

### 2.4. **Deletar categorias**

### `/api/products/section/categories/{id}/`

### Exemplo de Request:

Obs: Somente superuser ou staff tem permissão

```
DELETE api/products/section/categories/{id}/
Host: http://localhost:8000/api/products/section/categories/
Authorization: Token {token}
Content-type: application/json
```

### Corpo da Requisição:

```json
{}
```

### Exemplo de Response:

```
204 NO CONTENT
```

[ Voltar para os Endpoints ](#3-endpoints)

---

## 3. **Ingredients**

[ Voltar para os Endpoints ](#3-endpoints)

O objeto Ingredients é definido como:

| Campo | Tipo   | Descrição                      |
| ----- | ------ | ------------------------------ |
| id    | string | Identificador único do usuário |
| name  | string | Nome da categoria              |

---

### 3.1. **Criar ingrediente**

### `/api/products/section/ingredients/`

Obs: Somente superuser ou staff têm permissão.

### Exemplo de Request:

```
POST api/products/section/ingredients/
Host: http://localhost:8000/api/products/section/ingredients/
Authorization: Token {token}
Content-type: application/json
```

### Corpo da Requisição:

```json
{
  "name": "farinha"
}
```

### Exemplo de Response:

```
201 Created
```

```json
{
  "id": "7fdcce9b-03a3-4acf-a6e9-9c629c2552c8",
  "name": "farinha"
}
```

### Possíveis Erros:

| Código do Erro | Descrição                  |
| -------------- | -------------------------- |
| 403 Forbidden  | Usuário não tem permissão. |

[ Voltar para os Endpoints ](#3-endpoints)

---

### 3.2. **Listar ingredientes**

### `/api/products/section/ingredients/`

### Exemplo de Request:

```
GET api/products/section/ingredients/
Host: http://localhost:8000/api/products/section/ingredients/
Authorization: None
Content-type: application/json
```

### Corpo da Requisição:

```json
{}
```

### Exemplo de Response:

```
200 OK
```

```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "af04395f-a4dc-4c54-8075-befc427de4da",
      "name": "chocolate"
    },
    {
      "id": "a3147f64-cc8d-4a0d-806f-0bfbbff75db6",
      "name": "ovo"
    },
    {
      "id": "7fdcce9b-03a3-4acf-a6e9-9c629c2552c8",
      "name": "farinha"
    }
  ]
}
```

[ Voltar para os Endpoints ](#3-endpoints)

---

### 3.3. **Atualizar ingrediente**

### `/api/products/section/ingredients/{id}/`

### Exemplo de Request:

Obs: Somente superuser ou staff tem permissão

```
PATCH api/products/section/ingredients/{id}/
Host: http://localhost:8000/api/products/section/ingredients/{id}/
Authorization: Token {token}
Content-type: application/json
```

### Corpo da Requisição:

```json
{
  "name": "Farinha de trigo"
}
```

### Exemplo de Response:

```
200 OK
```

```json
{
  "id": "7fdcce9b-03a3-4acf-a6e9-9c629c2552c8",
  "name": "Farinha de trigo"
}
```

[ Voltar para os Endpoints ](#3-endpoints)

---

### 3.4. **Deletar ingrediente**

### `/api/products/section/ingredients/{id}/`

### Exemplo de Request:

Obs: Somente superuser ou staff tem permissão

```
DELETE api/products/section/ingredients/{id}/
Host: http://localhost:8000/api/products/section/ingredients/{id}/
Authorization: Token {token}
Content-type: application/json
```

### Corpo da Requisição:

```json
{}
```

### Exemplo de Response:

```
204 NO CONTENT
```

## [ Voltar para os Endpoints ](#3-endpoints)

## 4. **Orders**

[ Voltar para os Endpoints ](#3-endpoints)

O objeto orders é definido como:

| Campo           | Tipo    | Descrição                                               |
| --------------- | ------- | ------------------------------------------------------- |
| id              | string  | Identificador único do usuário                          |
| withdrawal_date | date    | Data de retirada do pedido                              |
| comment         | string  | Comentário do usuário sobre o pedido                    |
| total           | number  | Valor total pedido                                      |
| order_status    | string  | Situação do pedido                                      |
| is_finished     | boolean | Valor booleano que sinaliza se o pedido está finalizado |
| account         | obj     | Objeto que retorna o usuário que fez o pedido           |
| products        | array   | Lista de objetos dos produtos a serem encomendados      |

---

### 4.1. **Criar order**

### `/api/orders/create/`

Obs: withdrawal_date(data de retirada) deve ser pelo menos um dia de antecedência

### Exemplo de Request:

```
POST /api/orders/create/
Host: http://localhost:8000/api/orders/create/
Authorization: Token {token}
Content-type: application/json
```

### Corpo da Requisição:

```json
{
  "comment": "Quero produtos feito na hora!!!",
  "withdrawal_date": "2022-10-11",
  "products": [
    {
      "product": "650bb935-b872-4acf-866a-53d0badc61ea",
      "quantity": 50
    },
    {
      "product": "5881fad0-4eca-4bed-8a6b-9f673c34a946",
      "quantity": 50
    }
  ]
}
```

### Exemplo de Response:

```
201 Created
```

```json
{
  "id": "fc0ece29-1af0-467b-9eb5-a2470ab09700",
  "withdrawal_date": "2022-10-11T00:00:00Z",
  "comment": "Quero produtos feito na hora!!!",
  "total": 12325.0,
  "order_status": "Seu pedido está sendo analisado",
  "is_finished": false,
  "account": {
    "first_name": "Joao",
    "last_name": "client",
    "cellphone": "01988888882"
  },
  "products": [
    {
      "product": "650bb935-b872-4acf-866a-53d0badc61ea",
      "quantity": 50
    },
    {
      "product": "5881fad0-4eca-4bed-8a6b-9f673c34a946",
      "quantity": 50
    }
  ]
}
```

### Possíveis Erros:

| Código do Erro   | Descrição                                                                         |
| ---------------- | --------------------------------------------------------------------------------- |
| 400 Bad Request  | Erro caso o ID do produto não exista ou o pedido foi solicitado para o mesmo dia. |
| 401 Unauthorized | Credenciais não foram providas (token).                                           |

[ Voltar para os Endpoints ](#3-endpoints)

---

### 4.2. **Listar todos os orders**

### `/api/orders/`

Obs: Somente superuser ou staff têm permissão.

### Exemplo de Request:

```
POST /api/orders/create/
Host: http://localhost:8000/api/orders/
Authorization: Token {token}
Content-type: application/json
```

### Corpo da Requisição:

```json
{}
```

### Exemplo de Response:

```
200 OK
```

```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "fc0ece29-1af0-467b-9eb5-a2470ab09700",
      "withdrawal_date": "2022-10-11T00:00:00Z",
      "comment": "Quero produtos feito na hora!!!",
      "total": 12325.0,
      "order_status": "Seu pedido está sendo analisado",
      "is_finished": false,
      "account": {
        "first_name": "Joao",
        "last_name": "client",
        "cellphone": "01988888882"
      },
      "products": [
        {
          "product": "650bb935-b872-4acf-866a-53d0badc61ea",
          "quantity": 50
        },
        {
          "product": "5881fad0-4eca-4bed-8a6b-9f673c34a946",
          "quantity": 50
        }
      ]
    },
    {
      "id": "d1bc9a3a-b084-4369-9819-873621238e29",
      "withdrawal_date": "2022-10-11T00:00:00Z",
      "comment": "Quero produtos feito na hora!!!",
      "total": 12325.0,
      "order_status": "Seu pedido está sendo analisado",
      "is_finished": false,
      "account": {
        "first_name": "Joao",
        "last_name": "client",
        "cellphone": "01988888882"
      },
      "products": [
        {
          "product": "650bb935-b872-4acf-866a-53d0badc61ea",
          "quantity": 50
        },
        {
          "product": "5881fad0-4eca-4bed-8a6b-9f673c34a946",
          "quantity": 50
        }
      ]
    },
    {
      "id": "cbe17531-05d1-4275-8a21-76c45d534304",
      "withdrawal_date": "2022-10-11T00:00:00Z",
      "comment": "Quero produtos feito na hora!!!",
      "total": 12325.0,
      "order_status": "Seu pedido está sendo analisado",
      "is_finished": false,
      "account": {
        "first_name": "Joao",
        "last_name": "client",
        "cellphone": "01988888882"
      },
      "products": [
        {
          "product": "650bb935-b872-4acf-866a-53d0badc61ea",
          "quantity": 50
        },
        {
          "product": "5881fad0-4eca-4bed-8a6b-9f673c34a946",
          "quantity": 50
        }
      ]
    }
  ]
}
```

### Possíveis Erros:

| Código do Erro   | Descrição                                |
| ---------------- | ---------------------------------------- |
| 401 Unauthorized | Credenciais não foram providas (token).  |
| 403 Unauthorized | Erro caso o usuário não tenha permissão. |

[ Voltar para os Endpoints ](#3-endpoints)

---

### 4.3. **Listar orders do própio user**

### `/api/orders/owner/`

### Exemplo de Request:

```
GET /api/orders/
Host: http://localhost:8000/api/orders/owner/
Authorization: Token {token}
Content-type: application/json
```

### Corpo da Requisição:

```json
{}
```

### Exemplo de Response:

```
200 OK
```

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "b48eb424-b848-4f9b-ac80-5d6fa504278e",
      "withdrawal_date": "2022-10-11T00:00:00Z",
      "comment": "Quero produtos feito na hora!!!",
      "total": 48.0,
      "order_status": "Seu pedido está sendo analisado",
      "is_finished": false,
      "account": {
        "first_name": "regis",
        "last_name": "employee",
        "cellphone": "019154782652"
      },
      "products": [
        {
          "product": "650bb935-b872-4acf-866a-53d0badc61ea",
          "quantity": 10
        }
      ]
    },
    {
      "id": "ad75bcbd-d63d-44cc-8552-475aceab057e",
      "withdrawal_date": "2022-10-11T00:00:00Z",
      "comment": "Quero produtos feito na hora!!!",
      "total": 12325.0,
      "order_status": "Seu pedido está sendo analisado",
      "is_finished": false,
      "account": {
        "first_name": "regis",
        "last_name": "employee",
        "cellphone": "019154782652"
      },
      "products": [
        {
          "product": "650bb935-b872-4acf-866a-53d0badc61ea",
          "quantity": 50
        },
        {
          "product": "5881fad0-4eca-4bed-8a6b-9f673c34a946",
          "quantity": 50
        }
      ]
    }
  ]
}
```

### Possíveis Erros:

| Código do Erro   | Descrição                               |
| ---------------- | --------------------------------------- |
| 401 Unauthorized | Credenciais não foram providas (token). |

[ Voltar para os Endpoints ](#3-endpoints)

---

### 4.4. **Listar orders por data**

### `/api/orders/filter/?withdrawal_date={date}`

### Exemplo de Request:

Obs: Somente superuser ou staff.
Importante: Data deve ser passada nesse formato yyyy-mm-dd

```
GET /api/orders/filter/?withdrawal_date={date}
Host: http://localhost:8000/api/orders/filter/?withdrawal_date={date}
Authorization: Token {token}
Content-type: application/json
```

### Corpo da Requisição:

```json
{}
```

### Exemplo de Response:

```
200 OK
```

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "14074638-50b6-4813-b20a-03fb0751e8a8",
      "withdrawal_date": "2022-10-12T00:00:00Z",
      "comment": "Quero produtos feito na hora!!!",
      "total": 72.0,
      "order_status": "Seu pedido está sendo analisado",
      "is_finished": false,
      "account": {
        "first_name": "regis",
        "last_name": "employee",
        "cellphone": "019154782652"
      },
      "products": [
        {
          "product": "650bb935-b872-4acf-866a-53d0badc61ea",
          "quantity": 15
        }
      ]
    },
    {
      "id": "133ccfe1-4a88-41f0-b6e6-9aa2ad3e38a0",
      "withdrawal_date": "2022-10-12T00:00:00Z",
      "comment": "Quero produtos feito na hora!!!",
      "total": 48.0,
      "order_status": "Seu pedido está sendo analisado",
      "is_finished": false,
      "account": {
        "first_name": "regis",
        "last_name": "employee",
        "cellphone": "019154782652"
      },
      "products": [
        {
          "product": "650bb935-b872-4acf-866a-53d0badc61ea",
          "quantity": 10
        }
      ]
    }
  ]
}
```

### Possíveis Erros:

| Código do Erro   | Descrição                               |
| ---------------- | --------------------------------------- |
| 401 Unauthorized | Credenciais não foram providas (token). |

[ Voltar para os Endpoints ](#3-endpoints)

---

### 4.5. **Atualizar orders**

### `/api/orders/{id}/`

### Exemplo de Request:

Obs: Somente superuser ou própio user.

```
PATCH /api/orders/{id}/
Host: http://localhost:8000/api/orders/{id}/
Authorization: Token {token}
Content-type: application/json
```

### Corpo da Requisição:

```json
{{
	"comment": "Quero torta MUITO DELICIOSA",
	"products": [
		{
			"product": "5881fad0-4eca-4bed-8a6b-9f673c34a946",
			"quantity": 6
		}
	]
}}
```

### Exemplo de Response:

```
200 OK
```

```json
{
  "id": "14074638-50b6-4813-b20a-03fb0751e8a8",
  "withdrawal_date": "2022-10-12T00:00:00Z",
  "comment": "Quero torta MUITO DELICIOSA",
  "total": 39.0,
  "order_status": "Seu pedido está sendo analisado",
  "is_finished": false,
  "account": {
    "first_name": "regis",
    "last_name": "employee",
    "cellphone": "019154782652"
  },
  "products": [
    {
      "product": "5881fad0-4eca-4bed-8a6b-9f673c34a946",
      "quantity": 6
    }
  ]
}
```

### Possíveis Erros:

| Código do Erro   | Descrição                               |
| ---------------- | --------------------------------------- |
| 401 Unauthorized | Credenciais não foram providas (token). |
| 403 Forbidden    | Usuário não tem permissão.              |

[ Voltar para os Endpoints ](#3-endpoints)

---

### 4.6. **Atualizar status orders**

### `/api/orders/status/{id}/`

### Exemplo de Request:

Obs: Somente superuser ou própio user.

```
PATCH /api/orders/status/{id}/
Host: http://localhost:8000/api/orders/status/{id}/
Authorization: Token {token}
Content-type: application/json
```

### Corpo da Requisição:

Importante: usar nessa requisição "Pedido Confirmado" ou "Pedido Recusado" para alterar o status do pedido.

```json
{
  "order_status": "Pedido Confirmado"
}
```

### Exemplo de Response:

```
200 OK
```

```json
{
  "id": "fc0ece29-1af0-467b-9eb5-a2470ab09700",
  "order_status": "Pedido Confirmado"
}
```

### Possíveis Erros:

| Código do Erro   | Descrição                                                                   |
| ---------------- | --------------------------------------------------------------------------- |
| 400 Bad Request  | Erro retornado caso o valor passado seja diferente dos choices disponíveis. |
| 401 Unauthorized | Credenciais não foram providas (token).                                     |
| 403 Forbidden    | Usuário não tem permissão.                                                  |

[ Voltar para os Endpoints ](#3-endpoints)

---

### 4.7. **Deletar order**

### `/api/orders/{id}/`

### Exemplo de Request:

Obs: Somente superuser ou própio user.

```
DELETE /api/orders/{id}/
Host: http://localhost:8000/api/orders/{id}/
Authorization: Token {token}
Content-type: application/json
```

### Corpo da Requisição:

```json
{}
```

### Exemplo de Response:

```
204 NO CONTENT
```

### Possíveis Erros:

| Código do Erro   | Descrição                               |
| ---------------- | --------------------------------------- |
| 401 Unauthorized | Credenciais não foram providas (token). |
| 403 Forbidden    | Usuário não tem permissão.              |

[ Voltar para os Endpoints ](#3-endpoints)

---

## 4. Equipe

Alysson Marcos Colombo - [alysson1346](https://github.com/alysson1346) - SCRUM Master <br>
João Francisco Guarda Pozzer - [joaofranciscoguarda](https://github.com/joaofranciscoguarda) - Tech Leader <br>
Régis Theobald Silveira - [xregizzz](https://github.com/xregizzz) - Product Owner <br>
Kennedy Melo Barreto Muniz - [kennedybm](https://github.com/kennedybm) - Developer <br>
Paulo Vitor Leite Tobias - [pvitor7](https://github.com/pvitor7) - Developer <br>

[ Voltar para o topo ](#tabela-de-conteúdos)

---
