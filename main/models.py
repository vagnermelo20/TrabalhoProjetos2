from pyexpat import model
from django.db import models
from .opcoes import CONHECE, CONSELHO_OPCAO, ESCOLARIDADE_ESCOLHAS, REFERENCIA_FAMILIAR, TIPO_DE_REDE

class Aluno(models.Model):


    # FALTA FAZER 1.RESPONSAVEL LEGAL, 2.SITUACAO PROFISSIONAL, 3.SAUDE, 4.HÁBITOS ALIMENTARES, 5.GRUPOS COMUNITÁRIOS, 6.MORADIA E SANEAMENTO, 7.BENS, ELETRODOMÉSTICO E ELETRÔNICOS, 8.POLÍTICA DE ASSISTÊNCIA, 9.RENDA

    # PARTE DE IDENTIFICAÇÃO

    id = models.AutoField(primary_key=True)
    primeiro_nome = models.CharField(max_length = 45, blank = True, null = True)
    sobrenomes = models.CharField(max_length = 100, blank = True, null = True)
    idade = models.IntegerField()
    sexo = models.CharField(max_length = 1, blank = True, null = True)
    data_nascimento = models.DateField(blank = True, null = True)
    raca_cor = models.CharField(max_length = 45, blank = True, null = True)
    cpf = models.CharField() # Eu coloquei charfield porque tem . e - no cpf, depois eu coloco a logica certa no views
    telefone = models.CharField() # Eu coloquei charfield porque tem () e - no telefone, depois eu coloco a logica certa no views
    possui_whatsapp = models.BooleanField()
    estado_civil = models.CharField(max_length = 45)
    email = models.EmailField(max_length=255)
    turno = models.CharField()
    apadrinhado = models.BooleanField # perguntar como isso de apadrinhado funciona.
    # ProjetoIngressar = models.CharField(default="Projeto Alvo Certo")

    # PARTE DO ENDERECO

    cidade = models.CharField()
    estado = models.CharField()
    bairro = models.CharField()
    microrreiao = models.CharField()
    cep = models.CharField()  # Posso mudar para integerfield depois
    numero = models.IntegerField()
    extra = models.CharField(max_length = 255)

    # PARTE DA ESCOLARIDADE

    escolaridade = models.CharField(max_length = 45, choices = ESCOLARIDADE_ESCOLHAS)
    publico_ou_privado = models.CharField(max_length = 45, choices = TIPO_DE_REDE)
    ano_ou_periodo = models.CharField()
    turno = models.CharField()
    porque_nao_estuda = models.TextField() # Só para os que não estudam
    Quer_estudar = models.TextField()

    # PARTE DAS NOÇÕES COMPLEMENTARES

    conhece_o_eca = models.CharField(max_length = 45, choices = CONHECE)
    nocao_direitos_deveres = models.BooleanField()  # POSSUI ALGUMA NOÇÃO BÁSICA SOBRE DIREITOS E DEVERES DE CIDADANIA?
    referencia_familiar_pos_ou_neg = models.CharField(max_length = 45, choices = REFERENCIA_FAMILIAR) # SUA REFERÊNCIA DE FAMÍLIA É POSITIVA OU NEGATIVA?
    conhece_conselho_direito = models.CharField(max_length = 45, choices = CONHECE)
    qual_conselho = models.CharField(max_length = 45, choices = CONSELHO_OPCAO)
    conhece_foscar = models.CharField(max_length = 45, choices = CONHECE)

    # PARTE DA SITUACAO DE SAUDE

    plano_saude = models.BooleanField()
    qual_plano_saude = models.CharField(max_length = 100)
    teve_problema_saude = models.BooleanField()
    teve_acompanhamento_medico = models.BooleanField()
    ja_fez_cirurgia = models.BooleanField()
    



















    # cursos = models.ManyToManyField(Curso, related_name='professores')
    # materias = models.ManyToManyField(Materia, related_name='professores')

    # def __str__(self):
    #     return f"{self.primeiro_nome} {self.ultimo_nome}"