from rest_framework import serializers
from validate_docbr import CPF
import re

def validate_student(self, data):
    validate_cpf(data['cpf'])
    validate_name(data['name'])
    validate_phone_number(data['phone_number'])
    return data

def validate_cpf(cpf):
    cpf_validator = CPF()
    if not cpf_validator.validate(cpf):
        raise serializers.ValidationError({"cpf": ["CPF inválido."]})
    ''''
    if len(cpf) != 11:
        raise serializers.ValidationError({"cpf": ["CPF deve ter exatamente 11 dígitos."]})
    if not cpf.isdigit():
        raise serializers.ValidationError({"cpf": ["CPF deve conter apenas números."]})
    '''
    return cpf

def validate_name(name):
    if not name.isalpha():
        raise serializers.ValidationError({"name": ["Nome deve conter apenas letras."]})
    return name

def validate_phone_number(phone_number):
    if len(phone_number) != 13:
        raise serializers.ValidationError({"phone_number": ["Número de telefone deve ter 13 dígitos."]})
    '''
    if not phone_number.isdigit():
        raise serializers.ValidationError({"phone_number": ["Número de telefone deve conter apenas números."]})
    '''
    # Verificar o formato do número de telefone XX XXXXX-XXXX
    pattern = r'^\d{2} \d{5}-\d{4}$'
    if not re.match(pattern, phone_number):
        raise serializers.ValidationError({"phone_number": ["Número de telefone deve estar no formato XX XXXXX-XXXX."]})
    return phone_number