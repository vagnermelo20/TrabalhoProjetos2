ESCOLARIDADE_ESCOLHAS = [
    ('EDUCACAO_INFANTIL', 'Educação Infantil'),
    ('FUNDAMENTAL_INCOMPLETO', 'Fundamental Incompleto'),
    ('FUNDAMENTAL_COMPLETO', 'Fundamental Completo'),
    ('MEDIO_INCOMPLETO', 'Médio Incompleto'),
    ('MEDIO_COMPLETO', 'Médio Completo'),
    ('CURSO_TECNICO', 'Curso Técnico'),
    ('SUPERIOR_INCOMPLETO', 'Superior Incompleto'),
    ('SUPERIOR_COMPLETO', 'Superior Completo'),
    ('POS_GRADUACAO', 'Pós Graduação'),
    ('NAO_ACESSA_REDE_FORMAL', 'Não Acessa a Rede Formal de Ensino'),
]

TIPO_DE_REDE = [
    ('REDE_PUBLICA', 'Rede Pública'),
    ('REDE_PRIVADA', 'Rede Privada')
]

CONHECE = [
    ('CONHECO', 'Conheço'),
    ('OUVI_FALAR', 'Já ouvi falar'),
    ('NAO_CONHECO', 'Não Conheço')
]

CONSELHO_OPCAO = [
    ('CRIANCA', 'Criança'),
    ('ASSISTENCIA', 'Assistência'),
    ('IDOSO', 'Idoso'),
    ('SAUDE', 'Saúde'),
    ('EDUCACAO', 'Educação'),
]

REFERENCIA_FAMILIAR = [
    ('POSITIVA', 'Positiva'),
    ('NEGATIVA', 'Negativa'),
]

SITUACAO_PROFISSIONAL = [
    ('EMPREGO_FORMAL', 'Emprego Formal - CLT, Concurso, etc'),
    ('DESEMPREGADO', 'Desempregado(a)'),
    ('EMPREGO_INFORMAL', 'Emprego Informal/Biscates'),
    ('APOSENTADO', 'Aposentado(a)/Benefício'),
    ('MENOR_APRENDIZ', 'Menor Aprendiz'),
    ('JOVEM_APRENDIZ', 'Jovem Aprendiz'),
    ('APENAS_ESTUDA', 'Apenas Estuda'),
    ('DO_LAR', 'Do Lar'),
    ('OUTROS', 'Outros'),
]

TIPO_CASA = [
    ('PROPRIA', 'Própria'),
    ('ALUGADA', 'Alugada'),
    ('OCUPACAO', 'Ocupação'),
    ('CEDIDA', 'Cedida'),
    ('OUTRO', 'Outro'),
]

MATERIAL_CASA = [
    ('ALVENARIA', 'Alvenaria-Tijolos'),
    ('MADEIRA', 'Madeira'),
    ('TAIPA_REVESTIDA', 'Taipa Revestida'),
    ('TAIPA_NAO_REVESTIDA', 'Taipa Não Revestida'),
    ('MATERIAL_APROVEITADO', 'Material Aproveitado'),
    ('OUTRO', 'Outro'),
]

CONDICOES_AGUA = [
    ('REDE_PUBLICA', 'Rede Pública'),
    ('POCO', 'Poço'),
    ('RIO_ACUDE', 'Rio/Açude'),
    ('SEM_AGUA', 'Não tem disponibilidade de água'),
    ('OUTROS', 'Outros'),
]

DESTINO_LIXO = [
    ('COLETADO', 'Coletado'),
    ('QUEIMADO', 'Queimado/Enterrado'),
    ('CEU_ABERTO', 'Céu Aberto'),
    ('RIO', 'Rio'),
    ('OUTRO', 'Outro'),
]

DESTINO_FEZES = [
    ('REDE_GERAL', 'Sistema de Esgoto - Rede Geral'),
    ('FOSSA', 'Fossa'),
    ('CEU_ABERTO', 'Céu Aberto'),
    ('RIO', 'Rio'),
    ('OUTRO', 'Outro'),
]

RENDA_FAMILIAR = [
    ('ATE_MEIO', 'Até 1/2 SM'),
    ('UM_A_DOIS', '1 A 2 SM'),
    ('TRES_A_QUATRO', '03 A 04 SM'),
    ('ACIMA_QUATRO', 'Acima de 04 SM'),
]

CONDICOES_DESENVOLVIMENTO = [
    ('TDAH', 'Déficit de Atenção e Hiperatividade (TDAH)'),
    ('AUTISMO', 'Autismo'),
    ('DEPRESSAO', 'Depressão'),
    ('TRANSTORNO_BIPOLAR', 'Transtorno Bipolar'),
    ('DISTURBIO_BIPOLAR', 'Distúrbio Bipolar Comportamental'),
    ('DIFICULDADE_APRENDIZAGEM', 'Dificuldade de Aprendizagem'),
    ('ATRASO_MENTAL', 'Atraso Mental'),
]

GRUPOS_COMUNITARIOS = [
    ('COOPERATIVA', 'Cooperativa'),
    ('ASSOCIACAO', 'Associação'),
    ('GRUPO_RELIGIOSO', 'Grupo Religioso'),
    ('IGREJA', 'Igreja'),
    ('OUTRO', 'Outro'),
]

HABITOS_ALIMENTARES = [
    ('VERDURA', 'Verdura'),
    ('CARNE_VERMELHA', 'Carne Vermelha'),
    ('FRANGO', 'Frango'),
    ('PEIXE', 'Peixe'),
    ('LEITE', 'Leite'),
    ('FEIJAO', 'Feijão'),
]

SEXO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outro'),
]

ESTADO_CIVIL_CHOICES = [
    ('SOLTEIRO', 'Solteiro(a)'),
    ('CASADO', 'Casado(a)'),
    ('DIVORCIADO', 'Divorciado(a)'),
    ('VIUVO', 'Viúvo(a)'),
    ('UNIAO_ESTAVEL', 'União Estável'),
    ('OUTRO', 'Outro'),
]

TURNO_CHOICES = [
    ('MANHA', 'Manhã'),
    ('TARDE', 'Tarde'),
    ('NOITE', 'Noite'),
]

TURNO_ESCOLAR_CHOICES = [
    ('MANHA', 'Manhã'),
    ('TARDE', 'Tarde'),
    ('NOITE', 'Noite'),
    ('INTEGRAL', 'Integral'),
]

RACA_COR_CHOICES = [
    ('BRANCA', 'Branca'),
    ('PRETA', 'Preta'),
    ('PARDA', 'Parda'),
    ('AMARELA', 'Amarela'),
    ('INDIGENA', 'Indígena'),
    ('NAO_DECLARADO', 'Não Declarado'),
]

ESTADOS_BRASIL = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
]

ESTADO_EQUIPAMENTOS = [
    ('NOVOS', 'Novos'),
    ('USADOS', 'Usados'),
]
