from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
from .functions import *
from .limpieza import *
from rest_framework import generics
from . import serializer
from django.conf import settings
# Create your views here.
@api_view(['POST','GET'])
def transform_data(request):
    path_planilla=request.POST['path1']
    path_empleado=request.POST['path2']
    path_info_empleado=request.POST['path3']
    path_vacaciones=request.POST['path4']

    #obtener dataframe
    planilla = pd.read_csv(path_planilla)
    empleados = pd.read_csv(path_empleado)
    empleados_info = pd.read_csv(path_info_empleado)
    vacaciones = pd.read_csv(path_vacaciones)

    #valores ya limpios
    planilla=limpiar_planilla(planilla)
    empleados=limpiar_empleados(empleados)
    vacaciones=limpiar_vacaciones(vacaciones)
    empleados_info=limpiar_info(empleados_info)

    #procesar valores
    procesar_data(vacaciones,empleados,empleados_info,planilla)
    return Response({"message": "Datos procesados"})

class Empleados(generics.ListAPIView):
    queryset = REP_PERSONA.objects.all()
    serializer_class = serializer.PersonSerializer

class Vacaciones(generics.ListAPIView):
    queryset = REP_VACACIONES.objects.all()
    serializer_class = serializer.VacacionesSerializer

class Contratos(generics.ListAPIView):
    queryset = REP_TRABAJO.objects.all()
    serializer_class = serializer.ContratosSerializer

class Empresas(generics.ListAPIView):
    queryset = REP_EMPRESA.objects.all()
    serializer_class = serializer.EmpresaSerializer

@api_view(['GET'])
def error_empleado(request):
    dt1 = pd.read_csv(settings.EMPLEADOS_NAN)
    dt2 = pd.read_csv(settings.PLANILLA_NAN)
    rem_cols = []
    for x in dt1.columns:
        if str(x).__contains__('Unnamed'):
            rem_cols.append(x)
    dt1=dt1.drop(rem_cols,axis=1)
    rem_cols = []
    
    for x in dt2.columns:
        if str(x).__contains__('Unnamed'):
            rem_cols.append(x)
    dt2=dt2.drop(rem_cols,axis=1)
    return JsonResponse(dt1.to_dict())

@api_view(['GET'])
def error_planilla(request):
    dt2 = pd.read_csv(settings.PLANILLA_NAN)
    rem_cols = []
    for x in dt2.columns:
        if str(x).__contains__('Unnamed'):
            rem_cols.append(x)
    dt2=dt2.drop(rem_cols,axis=1)
    return JsonResponse(dt2.to_dict())