from django.db import models
from django.contrib.auth.models import User
from .opcoes import (CONHECE, CONSELHO_OPCAO, ESCOLARIDADE_ESCOLHAS, ESTADO_EQUIPAMENTOS, REFERENCIA_FAMILIAR, 
                    TIPO_DE_REDE, SITUACAO_PROFISSIONAL, TIPO_CASA, MATERIAL_CASA, 
                    CONDICOES_AGUA, DESTINO_LIXO, DESTINO_FEZES, RENDA_FAMILIAR,
                    CONDICOES_DESENVOLVIMENTO, GRUPOS_COMUNITARIOS, HABITOS_ALIMENTARES,
                    SEXO_CHOICES, ESTADO_CIVIL_CHOICES, TURNO_CHOICES, TURNO_ESCOLAR_CHOICES,
                    RACA_COR_CHOICES, ESTADOS_BRASIL)


class Responsavel(models.Model):
    """Informações do responsável legal"""
    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField(blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True, null=True)
    raca_cor = models.CharField(max_length=45, choices=RACA_COR_CHOICES, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    whatsapp = models.BooleanField(default=False)
    estado_civil = models.CharField(max_length=45, choices=ESTADO_CIVIL_CHOICES, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    """Modelo principal de aluno"""
    # Campos básicos de identificação
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    primeiro_nome = models.CharField(max_length=45)
    sobrenomes = models.CharField(max_length=100)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    data_nascimento = models.DateField()
    raca_cor = models.CharField(max_length=45, choices=RACA_COR_CHOICES)
    cpf = models.CharField(max_length=14, unique=True)  # formato: XXX.XXX.XXX-XX
    telefone = models.CharField(max_length=15)  # formato: (XX)XXXXX-XXXX
    possui_whatsapp = models.BooleanField(default=False)
    estado_civil = models.CharField(max_length=45, choices=ESTADO_CIVIL_CHOICES)
    email = models.EmailField(max_length=255, unique=True)
    turno = models.CharField(max_length=45, choices=TURNO_CHOICES)
    apadrinhado = models.BooleanField(default=False)
    ingressara_projeto = models.CharField(max_length=100)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Campos de endereço
    cidade = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=2, choices=ESTADOS_BRASIL, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    microrregiao = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(max_length=9, null=True, blank=True)  # formato: XXXXX-XXX
    numero = models.IntegerField(null=True, blank=True)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    
    # Campos de escolaridade
    nivel_escolaridade = models.CharField(max_length=45, choices=ESCOLARIDADE_ESCOLHAS, null=True, blank=True)
    tipo_rede_escolar = models.CharField(max_length=45, choices=TIPO_DE_REDE, null=True, blank=True)
    ano_ou_periodo = models.CharField(max_length=45, blank=True, null=True)
    turno_escolar = models.CharField(max_length=45, choices=TURNO_ESCOLAR_CHOICES, null=True, blank=True)
    motivo_nao_estuda = models.TextField(blank=True, null=True)
    deseja_estudar = models.TextField(blank=True, null=True)
    
    # Campos de situação profissional
    situacao_profissional = models.CharField(max_length=45, choices=SITUACAO_PROFISSIONAL, null=True, blank=True)
    profissao = models.CharField(max_length=100, blank=True, null=True)
    local_trabalho = models.CharField(max_length=100, blank=True, null=True)
    bairro_trabalho = models.CharField(max_length=100, blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    # Campos de noções complementares
    conhece_eca = models.CharField(max_length=45, choices=CONHECE, null=True, blank=True)
    nocao_direitos_deveres = models.BooleanField(default=False)
    referencia_familiar = models.CharField(max_length=45, choices=REFERENCIA_FAMILIAR, null=True, blank=True)
    conhece_conselho_direito = models.CharField(max_length=45, choices=CONHECE, null=True, blank=True)
    qual_conselho = models.CharField(max_length=45, choices=CONSELHO_OPCAO, blank=True, null=True)
    conhece_foscar = models.CharField(max_length=45, choices=CONHECE, null=True, blank=True)
    
    # Campos de situação de saúde
    plano_saude = models.BooleanField(default=False)
    qual_plano_saude = models.CharField(max_length=100, blank=True, null=True)
    teve_problema_saude = models.BooleanField(default=False)
    teve_acompanhamento_medico = models.BooleanField(default=False)
    ja_fez_cirurgia = models.BooleanField(default=False)
    problema_saude_atual = models.TextField(blank=True, null=True)
    deficiencia_fisica = models.BooleanField(default=False)
    qual_deficiencia = models.CharField(max_length=100, blank=True, null=True)
    condicao_desenvolvimento = models.CharField(max_length=45, choices=CONDICOES_DESENVOLVIMENTO, blank=True, null=True)
    local_atendimento_saude = models.CharField(max_length=100, blank=True, null=True)
    
    # Campos de moradia e saneamento
    tipo_casa = models.CharField(max_length=45, choices=TIPO_CASA, null=True, blank=True)
    material_casa = models.CharField(max_length=45, choices=MATERIAL_CASA, null=True, blank=True)
    risco_alagamento = models.BooleanField(default=False)
    risco_deslizamento = models.BooleanField(default=False)
    numero_comodos = models.IntegerField(null=True, blank=True)
    tem_divisoria_criancas_adultos = models.BooleanField(default=False)
    tem_banheiro = models.BooleanField(default=False)
    banheiro_dentro_casa = models.BooleanField(default=False)
    energia_eletrica = models.BooleanField(default=False)
    condicoes_agua = models.CharField(max_length=45, choices=CONDICOES_AGUA, null=True, blank=True)
    destino_lixo = models.CharField(max_length=45, choices=DESTINO_LIXO, null=True, blank=True)
    destino_fezes = models.CharField(max_length=45, choices=DESTINO_FEZES, null=True, blank=True)
    
    # Campos de bens e equipamentos
    possui_radio = models.BooleanField(default=False)
    possui_bicicleta = models.BooleanField(default=False)
    possui_tv = models.BooleanField(default=False)
    possui_computador = models.BooleanField(default=False)
    possui_celular = models.BooleanField(default=False)
    possui_fogao = models.BooleanField(default=False)
    possui_geladeira = models.BooleanField(default=False)
    possui_microondas = models.BooleanField(default=False)
    equipamentos_estado = models.CharField(max_length=45, choices=ESTADO_EQUIPAMENTOS, null=True, blank=True)
    equipamentos_recursos_proprios = models.BooleanField(default=False)
    equipamentos_presenteados = models.BooleanField(default=False)
    
    # Campos de assistência social e renda
    inscrito_cad_unico = models.BooleanField(default=False)
    beneficiario_bolsa_familia = models.BooleanField(default=False)
    recebe_auxilio_moradia = models.BooleanField(default=False)
    recebe_bpc = models.BooleanField(default=False)
    renda_familiar = models.CharField(max_length=45, choices=RENDA_FAMILIAR, null=True, blank=True)
    renda_per_capita = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Campos para hábitos alimentares e grupos comunitários
    habitos_alimentares = models.CharField(max_length=255, blank=True, null=True)
    grupos_comunitarios = models.CharField(max_length=255, blank=True, null=True)
    refeicoes_dia = models.IntegerField(null=True, blank=True)
    igreja_qual = models.CharField(max_length=100, blank=True, null=True)
    outro_grupo = models.CharField(max_length=100, blank=True, null=True)
    
    # Timestamps
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        ordering = ["primeiro_nome", "sobrenomes"]

    def __str__(self):
        return f"{self.primeiro_nome} {self.sobrenomes}"
    
    def nome_completo(self):
        return f"{self.primeiro_nome} {self.sobrenomes}"
    
    def endereco_completo(self):
        return f"{self.bairro}, {self.cidade}-{self.estado}, CEP: {self.cep}, Nº {self.numero}"

    def save(self, *args, **kwargs):
        if not self.pk and not self.usuario and self.email:
            # Cria um usuário automaticamente se não existir
            from django.contrib.auth.models import User
            username = self.email
            user = User.objects.create_user(
                username=username,
                email=self.email,
                password=None  # Será necessário um reset de senha
            )
            user.first_name = self.primeiro_nome
            user.last_name = self.sobrenomes
            user.is_active = True
            user.save()
            self.usuario = user
            
        super().save(*args, **kwargs)