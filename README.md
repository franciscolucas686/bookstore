# 📚 Bookstore API

Este é um projeto de backend desenvolvido em **Django** para gerenciar uma livraria (Bookstore). O sistema oferece estrutura modular para gerenciamento de pedidos, produtos e autenticação, com foco em boas práticas de desenvolvimento, deploy via Docker e integração contínua com GitHub Actions.

## 🚀 Tecnologias Utilizadas

- Python 3.12
- Django
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- GitHub Actions (CI/CD)
- Pytest (para testes)

## 📂 Estrutura do Projeto

bookstore/

├── settings.py # Configurações do projeto

├── urls.py # Rotas principais

├── wsgi.py # Configuração para servidores WSGI

├── asgi.py # Configuração para ASGI (opcional)

├── apps/

│ ├── order/ # App de pedidos

│ └── product/ # App de produtos

├── templates/ # Templates HTML (se aplicável)

└── manage.py # Gerenciador principal do Django


## ⚙️ Como Rodar Localmente

1. **Clone o projeto**:

```bash
git clone https://github.com/franciscolucas686/bookstore.git
cd bookstore
```

2. **Crie o arquivo .env com suas variáveis de ambiente (exemplo):**
   
```env
SECRET_KEY=your-secret-key
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1
DATABASE_URL=postgres://user:password@db:5432/dbname
```

3. **Suba os containers com Docker Compose:**

```bash
docker-compose up --build
```

4. **Acesse a aplicação:**

* API: http://localhost:8000/api/

* Admin: http://localhost:8000/admin/

## 🧪 Rodando os Testes

```bash
docker-compose exec web pytest
```

Ou, com Django:

```bash
docker-compose exec web python manage.py test
```

## 🛠️ CI/CD com GitHub Actions

O projeto utiliza um workflow de integração contínua que executa testes automaticamente a cada push na branch main.

## 📌 Funcionalidades Principais

Cadastro e listagem de produtos (livros)

Gerenciamento de pedidos

Integração com Django Admin

Autenticação JWT (em progresso)

Docker-ready para produção

## 📄 Licença
Este projeto está sob a licença MIT.
 ## 
 ##### Desenvolvido por Francisco Lucas
