from rest_framework import serializers

def validate_student(self, data):
    validate_cpf(data['cpf'])
    validate_name(data['name'])
    validate_phone_number(data['phone_number'])
    return data

def validate_cpf(cpf):
    if len(cpf) != 11:
        raise serializers.ValidationError({"cpf": ["CPF deve ter exatamente 11 dígitos."]})
    if not cpf.isdigit():
        raise serializers.ValidationError({"cpf": ["CPF deve conter apenas números."]})
    return cpf

def validate_name(name):
    if not name.isalpha():
        raise serializers.ValidationError({"name": ["Nome deve conter apenas letras."]})
    return name

def validate_phone_number(phone_number):
    if len(phone_number) != 13:
        raise serializers.ValidationError({"phone_number": ["Número de telefone deve ter 13 dígitos."]})
    if not phone_number.isdigit():
        raise serializers.ValidationError({"phone_number": ["Número de telefone deve conter apenas números."]})
    return phone_number