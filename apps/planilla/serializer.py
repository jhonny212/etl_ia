from rest_framework import serializers
from .models import *

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = REP_PERSONA
        fields = '__all__'

class VacacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = REP_VACACIONES
        fields = '__all__'

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = REP_EMPRESA
        fields = '__all__'
class ContratosSerializer(serializers.ModelSerializer):
    class Meta:
        model = REP_TRABAJO
        fields = '__all__'