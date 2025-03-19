from django import forms
from django.core.exceptions import ValidationError
from .models import Aluno, Responsavel
from .opcoes import (
    CONHECE, CONSELHO_OPCAO, ESCOLARIDADE_ESCOLHAS, ESTADO_EQUIPAMENTOS, REFERENCIA_FAMILIAR, 
    TIPO_DE_REDE, SITUACAO_PROFISSIONAL, TIPO_CASA, MATERIAL_CASA, 
    CONDICOES_AGUA, DESTINO_LIXO, DESTINO_FEZES, RENDA_FAMILIAR,
    CONDICOES_DESENVOLVIMENTO, GRUPOS_COMUNITARIOS, HABITOS_ALIMENTARES,
    SEXO_CHOICES, ESTADO_CIVIL_CHOICES, TURNO_CHOICES, TURNO_ESCOLAR_CHOICES,
    RACA_COR_CHOICES, ESTADOS_BRASIL
)

class ResponsavelForm(forms.ModelForm):
    class Meta:
        model = Responsavel
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'raca_cor': forms.Select(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'XXX.XXX.XXX-XX'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX)XXXXX-XXXX'}),
            'whatsapp': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if cpf:
            # Remover caracteres não numéricos
            cpf_numeros = ''.join(filter(str.isdigit, cpf))
            
            # Verificar se tem 11 dígitos
            if len(cpf_numeros) != 11:
                raise ValidationError('CPF deve conter 11 dígitos.')
            
            # Formatar como XXX.XXX.XXX-XX
            cpf_formatado = f"{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:]}"
            return cpf_formatado
        return cpf

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        if telefone:
            # Remover caracteres não numéricos
            tel_numeros = ''.join(filter(str.isdigit, telefone))
            
            # Verificar se tem entre 10 e 11 dígitos
            if not (10 <= len(tel_numeros) <= 11):
                raise ValidationError('Telefone deve ter entre 10 e 11 dígitos.')
            
            # Formatar como (XX)XXXXX-XXXX ou (XX)XXXX-XXXX
            if len(tel_numeros) == 11:
                tel_formatado = f"({tel_numeros[:2]}){tel_numeros[2:7]}-{tel_numeros[7:]}"
            else:
                tel_formatado = f"({tel_numeros[:2]}){tel_numeros[2:6]}-{tel_numeros[6:]}"
            return tel_formatado
        return telefone


class AlunoForm(forms.ModelForm):
    criar_responsavel = forms.BooleanField(
        required=False, 
        initial=False, 
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label="Cadastrar responsável"
    )
    
    class Meta:
        model = Aluno
        fields = '__all__'
        widgets = {
            # Campos básicos de identificação
            'primeiro_nome': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'sobrenomes': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'idade': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'sexo': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': True}),
            'raca_cor': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'XXX.XXX.XXX-XX', 'required': True}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX)XXXXX-XXXX', 'required': True}),
            'possui_whatsapp': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
            'turno': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'apadrinhado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ingressara_projeto': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'responsavel': forms.Select(attrs={'class': 'form-control'}),
            
            # Campos de endereço
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'microrregiao': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'XXXXX-XXX'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            
            # Campos de escolaridade
            'nivel_escolaridade': forms.Select(attrs={'class': 'form-control'}),
            'tipo_rede_escolar': forms.Select(attrs={'class': 'form-control'}),
            'ano_ou_periodo': forms.TextInput(attrs={'class': 'form-control'}),
            'turno_escolar': forms.Select(attrs={'class': 'form-control'}),
            'motivo_nao_estuda': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'deseja_estudar': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            
            # Campos de situação profissional
            'situacao_profissional': forms.Select(attrs={'class': 'form-control'}),
            'profissao': forms.TextInput(attrs={'class': 'form-control'}),
            'local_trabalho': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro_trabalho': forms.TextInput(attrs={'class': 'form-control'}),
            'salario': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            
            # Campos de noções complementares
            'conhece_eca': forms.Select(attrs={'class': 'form-control'}),
            'nocao_direitos_deveres': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'referencia_familiar': forms.Select(attrs={'class': 'form-control'}),
            'conhece_conselho_direito': forms.Select(attrs={'class': 'form-control'}),
            'qual_conselho': forms.Select(attrs={'class': 'form-control'}),
            'conhece_foscar': forms.Select(attrs={'class': 'form-control'}),
            
            # Campos de situação de saúde
            'plano_saude': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'qual_plano_saude': forms.TextInput(attrs={'class': 'form-control'}),
            'teve_problema_saude': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'teve_acompanhamento_medico': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ja_fez_cirurgia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'problema_saude_atual': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'deficiencia_fisica': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'qual_deficiencia': forms.TextInput(attrs={'class': 'form-control'}),
            'condicao_desenvolvimento': forms.Select(attrs={'class': 'form-control'}),
            'local_atendimento_saude': forms.TextInput(attrs={'class': 'form-control'}),
            
            # Campos de moradia e saneamento
            'tipo_casa': forms.Select(attrs={'class': 'form-control'}),
            'material_casa': forms.Select(attrs={'class': 'form-control'}),
            'risco_alagamento': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'risco_deslizamento': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'numero_comodos': forms.NumberInput(attrs={'class': 'form-control'}),
            'tem_divisoria_criancas_adultos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tem_banheiro': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'banheiro_dentro_casa': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'energia_eletrica': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'condicoes_agua': forms.Select(attrs={'class': 'form-control'}),
            'destino_lixo': forms.Select(attrs={'class': 'form-control'}),
            'destino_fezes': forms.Select(attrs={'class': 'form-control'}),
            
            # Campos de bens e equipamentos
            'possui_radio': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'possui_bicicleta': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'possui_tv': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'possui_computador': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'possui_celular': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'possui_fogao': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'possui_geladeira': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'possui_microondas': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'equipamentos_estado': forms.Select(attrs={'class': 'form-control'}),
            'equipamentos_recursos_proprios': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'equipamentos_presenteados': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
            # Campos de assistência social e renda
            'inscrito_cad_unico': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'beneficiario_bolsa_familia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'recebe_auxilio_moradia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'recebe_bpc': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'renda_familiar': forms.Select(attrs={'class': 'form-control'}),
            'renda_per_capita': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            
            # Campos para hábitos alimentares e grupos comunitários
            'habitos_alimentares': forms.TextInput(attrs={'class': 'form-control'}),
            'grupos_comunitarios': forms.TextInput(attrs={'class': 'form-control'}),
            'refeicoes_dia': forms.NumberInput(attrs={'class': 'form-control'}),
            'igreja_qual': forms.TextInput(attrs={'class': 'form-control'}),
            'outro_grupo': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        # Remover caracteres não numéricos
        cpf_numeros = ''.join(filter(str.isdigit, cpf))
        
        # Verificar se tem 11 dígitos
        if len(cpf_numeros) != 11:
            raise ValidationError('CPF deve conter 11 dígitos.')
        
        # Formatar como XXX.XXX.XXX-XX
        cpf_formatado = f"{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:]}"
        
        # Verificar se já existe outro aluno com este CPF
        if Aluno.objects.filter(cpf=cpf_formatado).exclude(id=self.instance.id if self.instance.id else None).exists():
            raise ValidationError('Já existe um aluno cadastrado com este CPF.')
            
        return cpf_formatado

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        # Remover caracteres não numéricos
        tel_numeros = ''.join(filter(str.isdigit, telefone))
        
        # Verificar se tem entre 10 e 11 dígitos
        if not (10 <= len(tel_numeros) <= 11):
            raise ValidationError('Telefone deve ter entre 10 e 11 dígitos.')
        
        # Formatar como (XX)XXXXX-XXXX ou (XX)XXXX-XXXX
        if len(tel_numeros) == 11:
            tel_formatado = f"({tel_numeros[:2]}){tel_numeros[2:7]}-{tel_numeros[7:]}"
        else:
            tel_formatado = f"({tel_numeros[:2]}){tel_numeros[2:6]}-{tel_numeros[6:]}"
        return tel_formatado

    def clean_cep(self):
        cep = self.cleaned_data.get('cep')
        if cep:
            # Remover caracteres não numéricos
            cep_numeros = ''.join(filter(str.isdigit, cep))
            
            # Verificar se tem 8 dígitos
            if len(cep_numeros) != 8:
                raise ValidationError('CEP deve conter 8 dígitos.')
            
            # Formatar como XXXXX-XXX
            cep_formatado = f"{cep_numeros[:5]}-{cep_numeros[5:]}"
            return cep_formatado
        return cep

    def clean_email(self):
        email = self.cleaned_data['email']
        # Verificar se já existe outro aluno com este email
        if Aluno.objects.filter(email=email).exclude(id=self.instance.id if self.instance.id else None).exists():
            raise ValidationError('Já existe um aluno cadastrado com este email.')
        return email 