import json
import re
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from .models import Curso, Materia, Professor, Aluno

class CursoCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            curso = Curso.objects.create(
                nome=data["nome"],
                carga_horaria=data["carga_horaria"],
                data_inicio=data["data_inicio"],
                data_fim=data["data_fim"]
            )

            # Link materias, professores, and alunos (if provided)
            if "materias" in data:
                curso.materias.set(data["materias"])  # List of Materia IDs
            if "professores" in data:
                curso.professores.set(data["professores"])  # List of Professor IDs
            if "alunos" in data:
                curso.alunos.set(data["alunos"])  # List of Aluno IDs

            return JsonResponse({"message": "Curso criado com sucesso!", "id": curso.id}, status=201)

        except KeyError as e:
            return JsonResponse({"error": f"Campo ausente: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


class MateriaCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            materia = Materia.objects.create(
                nome=data["nome"],
                carga_horaria=data["carga_horaria"]
            )

            # Linking Many-to-Many relationships
            if "cursos" in data:
                materia.cursos.set(data["cursos"])
            if "professores" in data:
                materia.professores.set(data["professores"])
            if "alunos" in data:
                materia.alunos.set(data["alunos"])

            return JsonResponse({"message": "Matéria criada com sucesso!", "id": materia.id}, status=201)

        except KeyError as e:
            return JsonResponse({"error": f"Campo ausente: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

class ProfessorCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            professor = Professor.objects.create(
                primeiro_nome=data["primeiro_nome"],
                ultimo_nome=data["ultimo_nome"],
                email=data["email"],
                senha_hashurada=data["senha_hashurada"],
                ano_comecou_ensinar=data["ano_comecou_ensinar"],
                salario=data["salario"],
                telefone=data.get("telefone", ""),
                data_nascimento=data["data_nascimento"]
            )

            # Linking Many-to-Many relationships
            if "cursos" in data:
                professor.cursos.set(data["cursos"])
            if "materias" in data:
                professor.materias.set(data["materias"])
            if "alunos" in data:
                professor.alunos.set(data["alunos"])

            return JsonResponse({"message": "Professor criado com sucesso!", "id": professor.id}, status=201)

        except KeyError as e:
            return JsonResponse({"error": f"Campo ausente: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

class AlunoCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            aluno = Aluno.objects.create(
                primeiro_nome=data["primeiro_nome"],
                ultimo_nome=data["ultimo_nome"],
                email=data["email"],
                senha_hashurada=data["senha_hashurada"],
                data_nascimento=data["data_nascimento"]
            )

            # Linking Many-to-Many relationships
            if "professores" in data:
                aluno.professores.set(data["professores"])
            if "cursos" in data:
                aluno.cursos.set(data["cursos"])
            if "materias" in data:
                aluno.materias.set(data["materias"])

            return JsonResponse({"message": "Aluno criado com sucesso!", "id": aluno.id}, status=201)

        except KeyError as e:
            return JsonResponse({"error": f"Campo ausente: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)



# class CursoListView(View):
#     def get(self, request):
#         cursos = Curso.objects.all()
#         materias = Materia.objects.all()
#         professores = Professor.objects.all()
#         alunos = Aluno.objects.all()
#         return render(request, "cursos.html", {
#             "cursos": cursos,
#             "materias": materias,
#             "professores": professores,
#             "alunos": alunos
#         })

#     def post(self, request):
#         curso = Curso.objects.create(
#             nome=request.POST["nome"],
#             carga_horaria=request.POST["carga_horaria"],
#             data_inicio=request.POST["data_inicio"],
#             data_fim=request.POST["data_fim"]
#         )

#         # Adiciona as matérias selecionadas
#         if "materias" in request.POST:
#             curso.materias.set(request.POST.getlist("materias"))

#         # Adiciona os professores selecionados
#         if "professores" in request.POST:
#             curso.professores.set(request.POST.getlist("professores"))

#         # Adiciona os alunos selecionados
#         if "alunos" in request.POST:
#             curso.alunos.set(request.POST.getlist("alunos"))

#         return redirect("cursos")
    

class MateriaListView(View):
    def get(self, request):
        materias = Materia.objects.all()
        return render(request, "materias.html", {"materias": materias})

    def post(self, request):
        Materia.objects.create(
            nome=request.POST["nome"],
            carga_horaria=request.POST["carga_horaria"]
        )
        return redirect("materias")

class ProfessorListView(View):
    def get(self, request):
        professores = Professor.objects.all()
        return render(request, "professores.html", {"professores": professores})

    def post(self, request):
        Professor.objects.create(
            primeiro_nome=request.POST["primeiro_nome"],
            ultimo_nome=request.POST["ultimo_nome"],
            email=request.POST["email"],
            senha_hashurada=request.POST["senha_hashurada"],
            ano_comecou_ensinar=request.POST["ano_comecou_ensinar"],
            salario=request.POST["salario"],
            telefone=request.POST.get("telefone", ""),
            data_nascimento=request.POST["data_nascimento"]
        )
        return redirect("professores")

class AlunoListView(View):
    def get(self, request):
        alunos = Aluno.objects.all()
        return render(request, "alunos.html", {"alunos": alunos})

    def post(self, request):
        Aluno.objects.create(
            primeiro_nome=request.POST["primeiro_nome"],
            ultimo_nome=request.POST["ultimo_nome"],
            email=request.POST["email"],
            senha_hashurada=request.POST["senha_hashurada"],
            data_nascimento=request.POST["data_nascimento"]
        )
        return redirect("alunos")
    




class CursoListView(View):
    def get(self, request):
        cursos = Curso.objects.all()
        if cursos.count() >= 1:
            paginator = Paginator(cursos, 10)  # Paginação (10 cursos por página)
            page_number = request.GET.get("page")
            page_obj = Paginator.get_page(page_number)
        
            return render(request, "cursos.html", {"cursos": page_obj})
        else:
          return render(request, "cursos.html", {"cursos": cursos})
class CursoCreateView(View):
    def post(self, request):
        try:
            nome = request.POST["nome"]
            carga_horaria = int(request.POST["carga_horaria"])
            data_inicio = request.POST["data_inicio"]
            data_fim = request.POST["data_fim"]

            # Criar curso
            curso = Curso.objects.create(
                nome=nome, carga_horaria=carga_horaria, data_inicio=data_inicio, data_fim=data_fim
            )

            # Adiciona relações Many-to-Many
            curso.materias.set(request.POST.getlist("materias", []))
            curso.professores.set(request.POST.getlist("professores", []))
            curso.alunos.set(request.POST.getlist("alunos", []))

            return redirect("cursos")
        except KeyError as e:
            return JsonResponse({"error": f"Campo ausente: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)