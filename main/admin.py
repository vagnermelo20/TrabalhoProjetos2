from django.contrib import admin
from .models import Aluno, Responsavel

class ResponsavelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone', 'whatsapp', 'email')
    search_fields = ('nome', 'cpf', 'telefone', 'email')

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('primeiro_nome', 'sobrenomes', 'cpf', 'telefone', 'idade', 'sexo', 'raca_cor')
    list_filter = ('sexo', 'raca_cor', 'estado_civil', 'apadrinhado', 'nivel_escolaridade', 'tipo_rede_escolar', 
                  'situacao_profissional', 'plano_saude', 'tipo_casa', 'renda_familiar')
    search_fields = ('primeiro_nome', 'sobrenomes', 'cpf', 'email', 'telefone', 'cidade', 'bairro')
    
    fieldsets = (
        ('Identificação', {
            'fields': (
                'primeiro_nome', 'sobrenomes', 'idade', 'sexo', 'data_nascimento', 
                'raca_cor', 'cpf', 'telefone', 'possui_whatsapp', 'estado_civil', 
                'email', 'turno', 'apadrinhado', 'ingressara_projeto', 'responsavel'
            )
        }),
        ('Endereço', {
            'fields': (
                'cidade', 'estado', 'bairro', 'microrregiao', 
                'cep', 'numero', 'complemento'
            )
        }),
        ('Escolaridade', {
            'fields': (
                'nivel_escolaridade', 'tipo_rede_escolar', 'ano_ou_periodo', 
                'turno_escolar', 'motivo_nao_estuda', 'deseja_estudar'
            )
        }),
        ('Situação Profissional', {
            'fields': (
                'situacao_profissional', 'profissao', 'local_trabalho', 
                'bairro_trabalho', 'salario'
            )
        }),
        ('Noções Complementares', {
            'fields': (
                'conhece_eca', 'nocao_direitos_deveres', 'referencia_familiar',
                'conhece_conselho_direito', 'qual_conselho', 'conhece_foscar'
            )
        }),
        ('Situação de Saúde', {
            'fields': (
                'plano_saude', 'qual_plano_saude', 'teve_problema_saude',
                'teve_acompanhamento_medico', 'ja_fez_cirurgia', 'problema_saude_atual',
                'deficiencia_fisica', 'qual_deficiencia', 'condicao_desenvolvimento',
                'local_atendimento_saude'
            )
        }),
        ('Moradia e Saneamento', {
            'fields': (
                'tipo_casa', 'material_casa', 'risco_alagamento', 'risco_deslizamento',
                'numero_comodos', 'tem_divisoria_criancas_adultos', 'tem_banheiro',
                'banheiro_dentro_casa', 'energia_eletrica', 'condicoes_agua',
                'destino_lixo', 'destino_fezes'
            )
        }),
        ('Bens e Equipamentos', {
            'fields': (
                'possui_radio', 'possui_bicicleta', 'possui_tv', 'possui_computador',
                'possui_celular', 'possui_fogao', 'possui_geladeira', 'possui_microondas',
                'equipamentos_estado', 'equipamentos_recursos_proprios', 'equipamentos_presenteados'
            )
        }),
        ('Assistência Social e Renda', {
            'fields': (
                'inscrito_cad_unico', 'beneficiario_bolsa_familia', 'recebe_auxilio_moradia',
                'recebe_bpc', 'renda_familiar', 'renda_per_capita'
            )
        }),
        ('Hábitos e Grupos', {
            'fields': (
                'refeicoes_dia', 'habitos_alimentares', 'grupos_comunitarios',
                'igreja_qual', 'outro_grupo'
            )
        }),
        ('Sistema', {
            'fields': (
                'usuario', 'criado_em', 'atualizado_em'
            ),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('criado_em', 'atualizado_em')

# Registrar os modelos no admin
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Responsavel, ResponsavelAdmin)
