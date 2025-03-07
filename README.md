<div align="center">
  <h1>
    <img src="./assets/hauntome.svg" width="40" height="40" alt="Hauntome Logo" style="vertical-align: middle; margin-right: 10px;">
    Hauntome API
  </h1>

  <p>Este projeto é uma API para gerenciamento de livros e usuários, desenvolvida com Django e Django REST Framework. Ele inclui autenticação via JWT, permissões personalizadas e documentação automática da API usando `drf-spectacular`.</p>
</div>

## Funcionalidades

- **Autenticação**: Registro e login de usuários com tokens JWT.
- **Gerenciamento de Livros**: CRUD de livros, com permissões para editar/excluir apenas os livros do usuário autenticado.
- **Documentação da API**: Documentação interativa gerada automaticamente com Swagger UI.

## Pré-requisitos

- Docker e Docker Compose instalados.
- Python 3.9 ou superior.

## Configuração

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/book-manager.git
   cd book-manager
   ```
2. Crie um arquivo .env na raiz do projeto com as seguintes variáveis de ambiente:
  ```bash
    SECRET_KEY=sua_chave_secreta_aqui
    DEBUG=True
  ```
3. Construa e inicie os containers:
  ```bash
    docker-compose up --build
  ```
4. Aplique as migrações:
  ```bash
    docker-compose exec web python manage.py migrate
  ```
5. Crie um superusuário:
  ```bash
    docker-compose exec web python manage.py createsuperuser
  ```

## Executando o Projeto

Após a configuração, o servidor estará disponível em http://localhost:8000/.

-    **Painel de Administração**: http://localhost:8000/admin/

-    **Documentação da API**: http://localhost:8000/api/docs/

## Rotas da API
### Autenticação

-    **Registro de Usuário**:

        **URL**: POST /api/auth/register/

        **Corpo da Requisição**:
        ```json
        {
          "username": "novousuario",
          "email": "novousuario@example.com",
          "password": "senhasegura123"
        }
        ```
-    **Login**:

        **URL**: POST /api/auth/login/

        **Corpo da Requisição**:
        ```json
        {
          "username": "novousuario",
          "password": "senhasegura123"
        } 
        ```
-    **Refresh Token**:

        **URL**: POST /api/auth/refresh/

        **Corpo da Requisição**:
        ```json
        {
          "refresh": "seu_refresh_token_aqui"
        } 
        ```

### Autenticação
-    **Listar Livros**:

        **URL**: GET /api/books/

        **Cabeçalho**: Authorization: Bearer <seu_access_token>

-    **Criar Livro**:

        **URL**: POST /api/books/

        **Cabeçalho**: Authorization: Bearer <seu_access_token>

        **Corpo da Requisição**:
        ```json
        {
          "title": "Dom Quixote",
          "author": "Miguel de Cervantes",
          "description": "Um clássico da literatura espanhola."
        } 
        ```
-    **Detalhes de um Livro**:

        **URL**: GET /api/books/<id>/

        **Cabeçalho**: Authorization: Bearer <seu_access_token>

-    **Atualizar Livro**:

        **URL**: PUT /api/books/<id>/
        **Cabeçalho**: Authorization: Bearer <seu_access_token>

        **Corpo da Requisição**:
        ```json
        {
          "title": "Dom Quixote - Edição Especial",
          "author": "Miguel de Cervantes",
          "description": "Um clássico da literatura espânica."
        } 
        ```
-    **Excluir Livro**:

        **URL**: DELETE /api/books/<id>/

        **Cabeçalho**: Authorization: Bearer <seu_access_token>

 
## Testes

Para executar os testes automatizados, use o seguinte comando:

```bash
  docker-compose exec web python3 manage.py test tests
```
