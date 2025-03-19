from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AlunoViewSet, ResponsavelViewSet,
    AlunoListView, AlunoDetailView, AlunoCreateView, AlunoUpdateView, AlunoDeleteView,
    home, dashboard, ResponsavelCreateView, ResponsavelUpdateView, ResponsavelDeleteView,
    export_alunos, register_view
)

# Configurar o router para a API REST
router = DefaultRouter()
router.register(r'api/alunos', AlunoViewSet)
router.register(r'api/responsaveis', ResponsavelViewSet)

urlpatterns = [
    # Páginas principais
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    
    # Rotas de alunos
    path('alunos/', AlunoListView.as_view(), name='aluno-list'),
    path('alunos/<int:pk>/', AlunoDetailView.as_view(), name='aluno-detail'),
    path('alunos/novo/', AlunoCreateView.as_view(), name='aluno-create'),
    path('alunos/cadastro/', AlunoCreateView.as_view(), name='aluno-create-old'),
    path('alunos/<int:pk>/editar/', AlunoUpdateView.as_view(), name='aluno-update'),
    path('alunos/<int:pk>/excluir/', AlunoDeleteView.as_view(), name='aluno-delete'),
    path('alunos/exportar/', export_alunos, name='aluno-export'),
    
    # Rotas de responsáveis
    path('responsaveis/novo/', ResponsavelCreateView.as_view(), name='responsavel-create'),
    path('responsaveis/<int:pk>/editar/', ResponsavelUpdateView.as_view(), name='responsavel-update'),
    path('responsaveis/<int:pk>/excluir/', ResponsavelDeleteView.as_view(), name='responsavel-delete'),
    
    # Autenticação
    path('accounts/register/', register_view, name='register'),
    
    # Incluir rotas automáticas da API
    path('', include(router.urls)),
]
