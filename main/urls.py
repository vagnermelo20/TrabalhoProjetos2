from django.urls import path
from .views import (
    CursoCreateView, MateriaCreateView, ProfessorCreateView, AlunoCreateView,  
    CursoListView, MateriaListView, ProfessorListView, AlunoListView
)

urlpatterns = [
    # These paths handle both GET (show list) and POST (add data via form)
    path('cursos/', CursoListView.as_view(), name='cursos'),
    path('materias/', MateriaListView.as_view(), name='materias'),
    path('professores/', ProfessorListView.as_view(), name='professores'),
    path('alunos/', AlunoListView.as_view(), name='alunos'),

    # API-style JSON POST routes (if you still need them separately)
    path('api/cursos/create/', CursoCreateView.as_view(), name='curso_create'),
    path('api/materias/create/', MateriaCreateView.as_view(), name='materia_create'),
    path('api/professores/create/', ProfessorCreateView.as_view(), name='professor_create'),
    path('api/alunos/create/', AlunoCreateView.as_view(), name='aluno_create'),
]
