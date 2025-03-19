from rest_framework import serializers
from .models import Aluno, Responsavel

class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = '__all__'

class AlunoSerializer(serializers.ModelSerializer):
    responsavel = ResponsavelSerializer(required=False, allow_null=True)
    nome_completo = serializers.ReadOnlyField()
    endereco_completo = serializers.ReadOnlyField()
    
    class Meta:
        model = Aluno
        fields = '__all__'
        read_only_fields = ('criado_em', 'atualizado_em', 'usuario')
    
    def create(self, validated_data):
        # Extract responsavel data if present
        responsavel_data = validated_data.pop('responsavel', None)
        
        # Create responsavel if data is provided
        if responsavel_data:
            responsavel = Responsavel.objects.create(**responsavel_data)
            # Create Aluno with responsavel
            aluno = Aluno.objects.create(responsavel=responsavel, **validated_data)
        else:
            # Create Aluno without responsavel
            aluno = Aluno.objects.create(**validated_data)
            
        return aluno
    
    def update(self, instance, validated_data):
        # Handle responsavel update if present
        if 'responsavel' in validated_data:
            responsavel_data = validated_data.pop('responsavel')
            if instance.responsavel:
                # Update existing responsavel
                responsavel = instance.responsavel
                for attr, value in responsavel_data.items():
                    setattr(responsavel, attr, value)
                responsavel.save()
            elif responsavel_data:
                # Create new responsavel
                responsavel = Responsavel.objects.create(**responsavel_data)
                instance.responsavel = responsavel
        
        # Update the basic fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance 