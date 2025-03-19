import json
import re
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.db.models import Q, Count
from .models import Aluno, Responsavel
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import AlunoSerializer, ResponsavelSerializer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .opcoes import (
    CONHECE, CONSELHO_OPCAO, ESCOLARIDADE_ESCOLHAS, ESTADO_EQUIPAMENTOS, REFERENCIA_FAMILIAR, 
    TIPO_DE_REDE, SITUACAO_PROFISSIONAL, TIPO_CASA, MATERIAL_CASA, 
    CONDICOES_AGUA, DESTINO_LIXO, DESTINO_FEZES, RENDA_FAMILIAR,
    CONDICOES_DESENVOLVIMENTO, GRUPOS_COMUNITARIOS, HABITOS_ALIMENTARES,
    SEXO_CHOICES, ESTADO_CIVIL_CHOICES, TURNO_CHOICES, TURNO_ESCOLAR_CHOICES,
    RACA_COR_CHOICES, ESTADOS_BRASIL
)
from .forms import AlunoForm, ResponsavelForm

# Função para registro de usuários
def register_view(request):
    """View para registro de novos usuários"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Conta criada com sucesso para {username}!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Manipuladores de erro
def handler404(request, exception):
    """Página não encontrada"""
    return render(request, '404.html', status=404)

def handler500(request):
    """Erro interno do servidor"""
    return render(request, '500.html', status=500)

# Exportação de alunos
def export_alunos(request):
    """Exportar dados de alunos em formato CSV ou Excel"""
    # Implementar lógica de exportação
    # Por enquanto, apenas redireciona para a lista
    messages.info(request, 'Funcionalidade de exportação será implementada em breve.')
    return redirect('aluno-list')

# class CursoCreateView(View):
#     def post(self, request):
#         try:
#             data = json.loads(request.body)
#             curso = Curso.objects.create(
#                 nome=data["nome"],
#                 carga_horaria=data["carga_horaria"],
#                 data_inicio=data["data_inicio"],
#                 data_fim=data["data_fim"]
#             )

#             # Link materias, professores, and alunos (if provided)
#             if "materias" in data:
#                 curso.materias.set(data["materias"])  # List of Materia IDs
#             if "professores" in data:
#                 curso.professores.set(data["professores"])  # List of Professor IDs
#             if "alunos" in data:
#                 curso.alunos.set(data["alunos"])  # List of Aluno IDs

#             return JsonResponse({"message": "Curso criado com sucesso!", "id": curso.id}, status=201)

#         except KeyError as e:
#             return JsonResponse({"error": f"Campo ausente: {str(e)}"}, status=400)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)


# class MateriaCreateView(View):
#     def post(self, request):
#         try:
#             data = json.loads(request.body)
#             materia = Materia.objects.create(
#                 nome=data["nome"],
#                 carga_horaria=data["carga_horaria"]
#             )

#             # Linking Many-to-Many relationships
#             if "cursos" in data:
#                 materia.cursos.set(data["cursos"])
#             if "professores" in data:
#                 materia.professores.set(data["professores"])
#             if "alunos" in data:
#                 materia.alunos.set(data["alunos"])

#             return JsonResponse({"message": "Matéria criada com sucesso!", "id": materia.id}, status=201)

#         except KeyError as e:
#             return JsonResponse({"error": f"Campo ausente: {str(e)}"}, status=400)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)

# class ProfessorCreateView(View):
#     def post(self, request):
#         try:
#             data = json.loads(request.body)
#             professor = Professor.objects.create(
#                 primeiro_nome=data["primeiro_nome"],
#                 ultimo_nome=data["ultimo_nome"],
#                 email=data["email"],
#                 senha_hashurada=data["senha_hashurada"],
#                 ano_comecou_ensinar=data["ano_comecou_ensinar"],
#                 salario=data["salario"],
#                 telefone=data.get("telefone", ""),
#                 data_nascimento=data["data_nascimento"]
#             )

#             # Linking Many-to-Many relationships
#             if "cursos" in data:
#                 professor.cursos.set(data["cursos"])
#             if "materias" in data:
#                 professor.materias.set(data["materias"])
#             if "alunos" in data:
#                 professor.alunos.set(data["alunos"])

#             return JsonResponse({"message": "Professor criado com sucesso!", "id": professor.id}, status=201)

#         except KeyError as e:
#             return JsonResponse({"error": f"Campo ausente: {str(e)}"}, status=400)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)

class AlunoCreateView(LoginRequiredMixin, CreateView):
    """Criação de um novo aluno"""
    model = Aluno
    form_class = AlunoForm
    template_name = 'main/aluno_form.html'
    success_url = reverse_lazy('aluno-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cadastrar Novo Aluno'
        context['responsavel_form'] = ResponsavelForm()
        context['opcoes'] = self.get_opcoes()
        return context
    
    def get_opcoes(self):
        """Retorna todas as opções para os campos de seleção"""
        return {
            'sexo_choices': SEXO_CHOICES,
            'raca_cor_choices': RACA_COR_CHOICES,
            'estado_civil_choices': ESTADO_CIVIL_CHOICES,
            'turno_choices': TURNO_CHOICES,
            'escolaridade_choices': ESCOLARIDADE_ESCOLHAS,
            'tipo_rede_choices': TIPO_DE_REDE,
            'turno_escolar_choices': TURNO_ESCOLAR_CHOICES,
            'situacao_profissional_choices': SITUACAO_PROFISSIONAL,
            'referencia_familiar_choices': REFERENCIA_FAMILIAR,
            'conhece_choices': CONHECE,
            'conselho_opcao_choices': CONSELHO_OPCAO,
            'condicoes_desenvolvimento_choices': CONDICOES_DESENVOLVIMENTO,
            'tipo_casa_choices': TIPO_CASA,
            'material_casa_choices': MATERIAL_CASA,
            'condicoes_agua_choices': CONDICOES_AGUA,
            'destino_lixo_choices': DESTINO_LIXO,
            'destino_fezes_choices': DESTINO_FEZES,
            'estado_equipamentos_choices': ESTADO_EQUIPAMENTOS,
            'renda_familiar_choices': RENDA_FAMILIAR,
            'habitos_alimentares_choices': HABITOS_ALIMENTARES,
            'grupos_comunitarios_choices': GRUPOS_COMUNITARIOS,
            'estados_brasil': ESTADOS_BRASIL,
        }
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        responsavel_form = None
        
        # Verificar se o usuário quer criar um responsável
        if 'criar_responsavel' in request.POST and request.POST.get('criar_responsavel') == 'on':
            responsavel_form = ResponsavelForm(request.POST)
            if form.is_valid() and responsavel_form.is_valid():
                return self.form_valid(form, responsavel_form)
            else:
                return self.form_invalid(form, responsavel_form)
        else:
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
    
    def form_valid(self, form, responsavel_form=None):
        self.object = form.save(commit=False)
        
        # Se tiver um responsável para ser criado
        if responsavel_form and responsavel_form.is_valid():
            responsavel = responsavel_form.save()
            self.object.responsavel = responsavel
            
        self.object.save()
        return redirect(self.success_url)
    
    def form_invalid(self, form, responsavel_form=None):
        context = self.get_context_data(form=form)
        if responsavel_form:
            context['responsavel_form'] = responsavel_form
        return self.render_to_response(context)

class AlunoListView(LoginRequiredMixin, ListView):
    """Listagem de alunos com filtros"""
    model = Aluno
    template_name = 'main/aluno_list.html'
    context_object_name = 'alunos'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Aluno.objects.all()
        
        # Filtros básicos
        nome = self.request.GET.get('nome')
        if nome:
            queryset = queryset.filter(
                Q(primeiro_nome__icontains=nome) | 
                Q(sobrenomes__icontains=nome)
            )
            
        cpf = self.request.GET.get('cpf')
        if cpf:
            queryset = queryset.filter(cpf__icontains=cpf)
            
        # Outros filtros
        sexo = self.request.GET.get('sexo')
        if sexo:
            queryset = queryset.filter(sexo=sexo)
            
        raca = self.request.GET.get('raca')
        if raca:
            queryset = queryset.filter(raca_cor=raca)
            
        escolaridade = self.request.GET.get('escolaridade')
        if escolaridade:
            queryset = queryset.filter(nivel_escolaridade=escolaridade)
            
        cidade = self.request.GET.get('cidade')
        if cidade:
            queryset = queryset.filter(cidade__icontains=cidade)
            
        return queryset.order_by('primeiro_nome', 'sobrenomes')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona as opções para os filtros
        context['sexo_choices'] = SEXO_CHOICES
        context['raca_choices'] = RACA_COR_CHOICES
        context['escolaridade_choices'] = ESCOLARIDADE_ESCOLHAS
        
        # Mantém os filtros aplicados
        context['filtros'] = self.request.GET.dict()
        return context

class AlunoDetailView(LoginRequiredMixin, DetailView):
    """Detalhes de um aluno específico"""
    model = Aluno
    template_name = 'main/aluno_detail.html'
    context_object_name = 'aluno'

class AlunoUpdateView(LoginRequiredMixin, UpdateView):
    """Atualização de um aluno existente"""
    model = Aluno
    form_class = AlunoForm
    template_name = 'main/aluno_form.html'
    success_url = reverse_lazy('aluno-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Aluno'
        context['is_update'] = True
        
        # Se já tem um responsável, carrega o form com os dados dele
        if self.object.responsavel:
            context['responsavel_form'] = ResponsavelForm(instance=self.object.responsavel)
        else:
            context['responsavel_form'] = ResponsavelForm()
            
        context['opcoes'] = self.get_opcoes()
        return context
    
    def get_opcoes(self):
        """Retorna todas as opções para os campos de seleção"""
        return {
            'sexo_choices': SEXO_CHOICES,
            'raca_cor_choices': RACA_COR_CHOICES,
            'estado_civil_choices': ESTADO_CIVIL_CHOICES,
            'turno_choices': TURNO_CHOICES,
            'escolaridade_choices': ESCOLARIDADE_ESCOLHAS,
            'tipo_rede_choices': TIPO_DE_REDE,
            'turno_escolar_choices': TURNO_ESCOLAR_CHOICES,
            'situacao_profissional_choices': SITUACAO_PROFISSIONAL,
            'referencia_familiar_choices': REFERENCIA_FAMILIAR,
            'conhece_choices': CONHECE,
            'conselho_opcao_choices': CONSELHO_OPCAO,
            'condicoes_desenvolvimento_choices': CONDICOES_DESENVOLVIMENTO,
            'tipo_casa_choices': TIPO_CASA,
            'material_casa_choices': MATERIAL_CASA,
            'condicoes_agua_choices': CONDICOES_AGUA,
            'destino_lixo_choices': DESTINO_LIXO,
            'destino_fezes_choices': DESTINO_FEZES,
            'estado_equipamentos_choices': ESTADO_EQUIPAMENTOS,
            'renda_familiar_choices': RENDA_FAMILIAR,
            'habitos_alimentares_choices': HABITOS_ALIMENTARES,
            'grupos_comunitarios_choices': GRUPOS_COMUNITARIOS,
            'estados_brasil': ESTADOS_BRASIL,
        }
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        
        # Verifica se tem um responsável
        responsavel_form = None
        if 'criar_responsavel' in request.POST and request.POST.get('criar_responsavel') == 'on':
            if self.object.responsavel:
                responsavel_form = ResponsavelForm(request.POST, instance=self.object.responsavel)
            else:
                responsavel_form = ResponsavelForm(request.POST)
                
            if form.is_valid() and responsavel_form.is_valid():
                return self.form_valid(form, responsavel_form)
            else:
                return self.form_invalid(form, responsavel_form)
        else:
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
    
    def form_valid(self, form, responsavel_form=None):
        self.object = form.save(commit=False)
        
        # Se tiver um responsável para ser criado/atualizado
        if responsavel_form and responsavel_form.is_valid():
            responsavel = responsavel_form.save()
            self.object.responsavel = responsavel
            
        self.object.save()
        return redirect(self.success_url)
    
    def form_invalid(self, form, responsavel_form=None):
        context = self.get_context_data(form=form)
        if responsavel_form:
            context['responsavel_form'] = responsavel_form
        return self.render_to_response(context)

class AlunoDeleteView(LoginRequiredMixin, DeleteView):
    """Remover um aluno"""
    model = Aluno
    template_name = 'main/aluno_confirm_delete.html'
    success_url = reverse_lazy('aluno-list')

# Views simples para a homepage e dashboard
@login_required
def home(request):
    """View para a página inicial"""
    total_alunos = Aluno.objects.count()
    homens = Aluno.objects.filter(sexo='M').count()
    mulheres = Aluno.objects.filter(sexo='F').count()
    
    context = {
        'total_alunos': total_alunos,
        'homens': homens,
        'mulheres': mulheres,
    }
    
    return render(request, 'main/home.html', context)

@login_required
def dashboard(request):
    """Dashboard com estatísticas"""
    total_alunos = Aluno.objects.count()
    
    # Contagem por sexo
    homens = Aluno.objects.filter(sexo='M').count()
    mulheres = Aluno.objects.filter(sexo='F').count()
    
    # Contagem por raça/cor
    dados_raca = []
    for codigo, nome in RACA_COR_CHOICES:
        count = Aluno.objects.filter(raca_cor=codigo).count()
        if count > 0:
            dados_raca.append({'nome': nome, 'quantidade': count})
    
    # Contagem por escolaridade
    dados_escolaridade = []
    for codigo, nome in ESCOLARIDADE_ESCOLHAS:
        count = Aluno.objects.filter(nivel_escolaridade=codigo).count()
        if count > 0:
            dados_escolaridade.append({'nome': nome, 'quantidade': count})
    
    context = {
        'total_alunos': total_alunos,
        'homens': homens,
        'mulheres': mulheres,
        'dados_raca': json.dumps(dados_raca),
        'dados_escolaridade': json.dumps(dados_escolaridade),
    }
    
    return render(request, 'main/dashboard.html', context)

# API ViewSets
class AlunoViewSet(viewsets.ModelViewSet):
    """ViewSet para API de Alunos"""
    queryset = Aluno.objects.all().order_by('primeiro_nome')
    serializer_class = AlunoSerializer
    filterset_fields = ['sexo', 'raca_cor', 'apadrinhado', 'estado_civil', 'nivel_escolaridade', 'situacao_profissional']
    search_fields = ['primeiro_nome', 'sobrenomes', 'cpf', 'telefone', 'email', 'cidade', 'bairro']
    
    @action(detail=False, methods=['get'])
    def estatisticas(self, request):
        """Endpoint para estatísticas básicas dos alunos"""
        total = Aluno.objects.count()
        por_sexo = {
            'masculino': Aluno.objects.filter(sexo='M').count(),
            'feminino': Aluno.objects.filter(sexo='F').count(),
            'outro': Aluno.objects.exclude(sexo__in=['M', 'F']).count()
        }
        por_raca = {}
        for raca_choice in dict(RACA_COR_CHOICES).items():
            por_raca[raca_choice[1]] = Aluno.objects.filter(raca_cor=raca_choice[0]).count()
        
        por_escolaridade = {}
        for esc_choice in dict(ESCOLARIDADE_ESCOLHAS).items():
            por_escolaridade[esc_choice[1]] = Aluno.objects.filter(nivel_escolaridade=esc_choice[0]).count()
        
        por_situacao_prof = {}
        for sit_choice in dict(SITUACAO_PROFISSIONAL).items():
            por_situacao_prof[sit_choice[1]] = Aluno.objects.filter(situacao_profissional=sit_choice[0]).count()
        
        return Response({
            'total': total,
            'por_sexo': por_sexo,
            'por_raca': por_raca,
            'por_escolaridade': por_escolaridade,
            'por_situacao_profissional': por_situacao_prof
        })

class ResponsavelViewSet(viewsets.ModelViewSet):
    """ViewSet para API de Responsáveis"""
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer
    search_fields = ['nome', 'cpf', 'telefone', 'email']

# Views de Responsáveis
class ResponsavelCreateView(LoginRequiredMixin, CreateView):
    """Criação de um novo responsável"""
    model = Responsavel
    form_class = ResponsavelForm
    template_name = 'main/responsavel_form.html'
    success_url = reverse_lazy('aluno-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cadastrar Novo Responsável'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Responsável cadastrado com sucesso!')
        return super().form_valid(form)
    
class ResponsavelUpdateView(LoginRequiredMixin, UpdateView):
    """Atualização de um responsável existente"""
    model = Responsavel
    form_class = ResponsavelForm
    template_name = 'main/responsavel_form.html'
    success_url = reverse_lazy('aluno-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Responsável'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Responsável atualizado com sucesso!')
        return super().form_valid(form)

class ResponsavelDeleteView(LoginRequiredMixin, DeleteView):
    """Remover um responsável"""
    model = Responsavel
    template_name = 'main/responsavel_confirm_delete.html'
    success_url = reverse_lazy('aluno-list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Responsável removido com sucesso!')
        return super().delete(request, *args, **kwargs)