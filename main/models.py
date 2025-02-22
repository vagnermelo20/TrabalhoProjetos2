from django.db import models

class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, db_index=True)
    carga_horaria = models.PositiveIntegerField()
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return self.nome


class Materia(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, db_index=True)
    carga_horaria = models.PositiveIntegerField()
    cursos = models.ManyToManyField(Curso, related_name="materias")  

    def __str__(self):
        return self.nome


class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    primeiro_nome = models.CharField(max_length=50)
    ultimo_nome = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=225, db_index=True)
    senha_hashurada = models.TextField()
    ano_comecou_ensinar = models.PositiveIntegerField()
    salario = models.FloatField()
    telefone = models.CharField(max_length=25, blank=True, null=True)
    data_nascimento = models.DateField()
    cursos = models.ManyToManyField(Curso, related_name='professores')
    materias = models.ManyToManyField(Materia, related_name='professores')

    def __str__(self):
        return f"{self.primeiro_nome} {self.ultimo_nome}"


class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    primeiro_nome = models.CharField(max_length=50)
    ultimo_nome = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=225, db_index=True)
    senha_hashurada = models.TextField()
    data_nascimento = models.DateField()
    professores = models.ManyToManyField(Professor, related_name='alunos')
    cursos = models.ManyToManyField(Curso, related_name='alunos')
    materias = models.ManyToManyField(Materia, related_name='alunos')

    def __str__(self):
        return f"{self.primeiro_nome} {self.ultimo_nome}"
