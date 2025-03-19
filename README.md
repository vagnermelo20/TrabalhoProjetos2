# Sistema de Gerenciamento de Alunos

Um sistema completo para gerenciar informações de alunos, incluindo dados pessoais, educacionais, socioeconômicos e de saúde.

## Características

- Cadastro completo de alunos com informações detalhadas
- Interface administrativa para gestão de dados
- Dashboard com estatísticas e visualizações
- API REST para integração com outros sistemas
- Sistema de autenticação e permissões
- Interface responsiva e amigável

## Tecnologias Utilizadas

- Django 5.1
- Django REST Framework
- SQLite (desenvolvimento) / PostgreSQL (produção)
- Bootstrap 5 (frontend)
- JavaScript / Chart.js (visualizações)

## Requisitos

- Python 3.9+
- Pip (gerenciador de pacotes do Python)
- Virtualenv (recomendado)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/sistema-alunos.git
cd sistema-alunos
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente (opcional, para produção):
```bash
export DJANGO_SECRET_KEY='sua-chave-secreta'
export DJANGO_DEBUG='False'
export DJANGO_ALLOWED_HOSTS='seu-dominio.com,www.seu-dominio.com'
# ... outras variáveis
```

5. Execute as migrações:
```bash
python manage.py migrate
```

6. Crie um superusuário:
```bash
python manage.py createsuperuser
```

7. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

8. Acesse o sistema em: http://localhost:8000

## Estrutura do Projeto

O projeto segue a estrutura padrão do Django, com os seguintes componentes principais:

- `main/` - Aplicativo principal
  - `models.py` - Definição dos modelos de dados
  - `views.py` - Lógica de visualização
  - `urls.py` - Configuração de rotas
  - `serializers.py` - Serialização de dados para API
  - `admin.py` - Configuração do painel administrativo
  - `templates/` - Templates HTML
  - `static/` - Arquivos estáticos

- `project/` - Configuração do projeto
  - `settings.py` - Configurações gerais
  - `urls.py` - Rotas principais

## Uso da API

O sistema fornece uma API REST completa para integração com outros sistemas. Endpoints principais:

- `/api/alunos/` - CRUD de alunos
- `/api/alunos/estatisticas/` - Estatísticas sobre os alunos
- `/api/habitos-alimentares/` - Hábitos alimentares
- `/api/grupos-comunitarios/` - Grupos comunitários
- `/api/enderecos/` - Endereços
- `/api/responsaveis/` - Responsáveis legais
- `/api/escolaridades/` - Dados de escolaridade
- `/api/situacoes-profissionais/` - Situações profissionais

Todas as requisições à API requerem autenticação.

## Produção

Para implantar em produção, recomenda-se:

1. Usar PostgreSQL ou outro banco de dados robusto
2. Configurar variáveis de ambiente adequadamente
3. Usar Gunicorn ou uWSGI como servidor de aplicação
4. Configurar Nginx ou Apache como proxy reverso
5. Coletar arquivos estáticos:
```bash
python manage.py collectstatic
```

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Faça push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

## Contato

Para dúvidas ou sugestões, entre em contato através de [seu-email@exemplo.com].
