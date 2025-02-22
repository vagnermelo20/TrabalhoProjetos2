from django.contrib import admin
from .models import Curso, Materia, Professor, Aluno
# Register your models here.

admin.site.register(Curso)
admin.site.register(Materia)
admin.site.register(Professor)
admin.site.register(Aluno)