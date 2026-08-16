# ComputerShop - Loja Online de Peças de Computador

Uma plataforma e-commerce desenvolvida em Django para venda de componentes e periféricos de computador. O projeto é uma aplicação web full-stack que permite gerenciar catálogo de produtos, carrinho de compras e processamento de pedidos.

## 🎯 Objetivo

Criar uma loja online moderna e eficiente especializada na venda de peças e componentes de computador, oferecendo aos clientes uma experiência de compra intuitiva com catálogo bem organizado, carrinho de compras funcional e processamento seguro de pedidos.

## 🔧 Stack Técnico

| Componente | Tecnologia | Versão |
|-----------|-----------|--------|
| **Backend** | Django | 6.1 |
| **Banco de Dados** | SQLite (dev) / PostgreSQL (prod) | - |
| **Frontend** | HTML5 + CSS3 + JavaScript | ES6+ |
| **Servidor** | Django Development Server | - |
| **Python** | Python | 3.10+ |

## 📋 Pré-requisitos

- Python 3.10+
- pip
- Git (para controle de versão)

## 🚀 Configuração Rápida

### 1. Clone o repositório
```bash
git clone <seu-repositorio>
cd projeto
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv
```

**Ativar ambiente virtual:**

Windows (PowerShell):
```bash
venv\Scripts\Activate.ps1
```

Windows (CMD):
```bash
venv\Scripts\activate.bat
```

macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
pip install python-dotenv  # Para gerenciar variáveis de ambiente
```

### 4. Configure variáveis de ambiente
```bash
# Copie o arquivo de exemplo
copy .env.example .env  # Windows
cp .env.example .env    # macOS/Linux

# Edite o .env com suas configurações
```

### 5. Execute as migrações do banco de dados
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crie um superusuário (acesso ao admin)
```bash
python manage.py createsuperuser
```

Você será solicitado a criar credenciais para acessar o painel administrativo.

### 7. Inicie o servidor de desenvolvimento
```bash
python manage.py runserver
```

**Acessos:**
- 🌐 Site: http://localhost:8000
- 🔐 Admin: http://localhost:8000/admin

## 📂 Estrutura do Projeto

```
projeto/
├── projeto/                 # Configurações principais do Django
│   ├── settings.py         # Configurações do projeto (BD, apps, middleware)
│   ├── urls.py             # Rotas principais da aplicação
│   ├── views.py            # Views gerais (ex: homepage)
│   ├── wsgi.py             # Configuração WSGI para deploy
│   ├── asgi.py             # Configuração ASGI para async
│   └── __init__.py
│
├── produtos/                # App Django - Gestão de Produtos
│   ├── models.py           # Modelos de dados (Produto, Categoria, etc)
│   ├── views.py            # Views do app (lista, detalhe, busca)
│   ├── urls.py             # Rotas específicas do app
│   ├── admin.py            # Configuração do painel administrativo
│   ├── apps.py             # Configuração da aplicação
│   ├── tests.py            # Testes unitários
│   ├── migrations/         # Migrações de banco de dados
│   └── __init__.py
│
├── templates/               # Templates HTML
│   ├── home/
│   │   └── index.html      # Página inicial
│   ├── produtos/
│   │   └── produtos.html   # Listagem de produtos
│   └── ...
│
├── static/                  # Arquivos estáticos (CSS, JS, imagens)
│   ├── css/
│   ├── js/
│   └── images/
│
├── manage.py               # CLI do Django
├── requirements.txt        # Dependências do projeto
├── .env.example            # Exemplo de variáveis de ambiente
├── .gitignore              # Arquivos ignorados pelo Git
└── README.md               # Este arquivo
```

## 🌐 Rotas Disponíveis

| Rota | Método | Descrição | Autenticação |
|------|--------|-----------|--------------|
| `/` | GET | Página inicial da loja | Não |
| `/produtos/` | GET | Listagem de produtos | Não |
| `/produtos/<id>/` | GET | Detalhe do produto | Não |
| `/admin/` | GET/POST | Painel administrativo | Sim (Superuser) |

## 💾 Modelos de Dados

### Produtos (A implementar)
- `id` - Identificador único
- `nome` - Nome do produto
- `descricao` - Descrição detalhada
- `preco` - Preço em R$
- `categoria` - Categoria (CPU, RAM, SSD, etc)
- `estoque` - Quantidade disponível
- `imagem` - Imagem do produto
- `criado_em` - Data de criação
- `atualizado_em` - Data de atualização

### Categorias (A implementar)
- `id` - Identificador único
- `nome` - Nome da categoria
- `descricao` - Descrição

## 🔧 Configurações Importantes

### Desenvolvimento
```env
DEBUG=True
SECRET_KEY=sua-chave-secreta-de-desenvolvimento
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### Produção
```env
DEBUG=False
SECRET_KEY=chave-secreta-segura-gerada
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
DATABASE_URL=postgresql://user:password@host:port/database
```

## 🛠️ Ferramentas de Desenvolvimento

```bash
# Executar testes
python manage.py test

# Criar um super-usuário
python manage.py createsuperuser

# Verificar problemas de segurança
python manage.py check --deploy

# Limpar cache de migrações
python manage.py makemigrations --empty products --name initial_migration

# Shell interativo Django
python manage.py shell
```

## 📚 Dependências Principais

```
Django==6.1              # Framework web Python
asgiref==3.12.1          # Suporte para ASGI/async
python-dotenv==1.0.0     # Gerenciar variáveis de ambiente
```

## 🔒 Segurança

- ✅ CSRF Protection ativada
- ✅ Password validation configurada
- ✅ XFrame protection ativada
- ⚠️ SECRET_KEY em `.env` (não compartilhar)
- ⚠️ DEBUG=False obrigatório em produção

## 📖 Documentação Django

- [Django 6.1 Documentation](https://docs.djangoproject.com/en/6.1/)
- [Django Models Documentation](https://docs.djangoproject.com/en/6.1/topics/db/models/)
- [Django Views Documentation](https://docs.djangoproject.com/en/6.1/topics/http/views/)
- [Django Admin Documentation](https://docs.djangoproject.com/en/6.1/ref/contrib/admin/)

## 🚀 Próximas Etapas (Roadmap)

- [ ] Implementar modelos de dados (Produto, Categoria, Pedido)
- [ ] Criar sistema de autenticação de usuários
- [ ] Implementar carrinho de compras com sessões
- [ ] Adicionar sistema de pagamento (Stripe/PagSeguro)
- [ ] Criar sistema de pedidos e rastreamento
- [ ] Implementar busca e filtros de produtos
- [ ] Adicionar sistema de avaliações e comentários
- [ ] Desenvolver painel de controle do admin customizado
- [ ] Implementar sistema de notificações por email
- [ ] Deploy em produção (Heroku/AWS/DigitalOcean)

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Gabriel Cherem**
- GitHub: [@seu-usuario](https://github.com/seu-usuario)
- Email: seu-email@example.com

## 📞 Suporte

Para dúvidas ou problemas, abra uma [Issue](https://github.com/seu-usuario/projeto/issues) no repositório.

---

**Última atualização:** Agosto de 2026
