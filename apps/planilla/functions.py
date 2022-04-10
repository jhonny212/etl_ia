from ast import Dict
from cmath import inf
import pandas as pd
import re
from datetime import datetime
from .models import *
from django.db import connection 

def procesar_empleado(empleados:pd.DataFrame):
    list_empleados = []
    dict_date = {}
    empleados=empleados.drop_duplicates(subset=['DPI'])
    for dpi,nit,telefono,correo,orden_cedula,registro_cedula,f1,f2 in zip(
            empleados['DPI'],
            empleados['NIT'],
            empleados['Telefono'],
            empleados['Correo_Electronico_trabajo'],
            empleados['Cedula_Orden'],
            empleados['Cedula_Registro'],
            empleados['Fecha_Inicial'],
            empleados['Fecha_Final']
        ):
        bool = REP_PERSONA.objects.filter(dpi=dpi).exists()
        if not bool:
            tmp = REP_PERSONA(
                dpi=dpi,
                nit=nit,
                telefono=telefono,
                orden_cedula=orden_cedula,
                registro_cedula=registro_cedula,
                correo_electronico=correo
            )
            list_empleados.append(tmp)
        dict_date[dpi]=[f1,f2]
    REP_PERSONA.objects.bulk_create(list_empleados)
    return dict_date

def procesar_info_empleados(info:pd.DataFrame):
    list_info = []
    #	Direccion_Residencia	Genero	Nacimiento	DPI
    for pn,sn,pa,sa,ac,dt,mt,dr,g,n,dpi in zip(
            info['Primer_Nombre'],
            info['Segundo_Nombre'],
            info['Primer_Apellido'],
            info['Segundo_Apellido'],
            info['Apellido_Casada'],
            info['Departamento_trabajo'],
            info['Municipio_trabajo'],
            info['Direccion_Residencia'],
            info['Genero'],
            info['Nacimiento'],
            info['DPI']
        ):
        persona=REP_PERSONA.objects.filter(
            dpi=dpi
        ).first()
        info_tmp = REP_INFO_PERSONA.objects.filter(persona__dpi=dpi).first()
        if persona is not None and info_tmp is None:
            persona_info = REP_INFO_PERSONA(
                primer_nombre=pn,
                segundo_nombre=sn,
                primer_apellido=pa,
                segundo_apellido=sa,
                apellido_casada=ac,
                fecha_nacimiento =n,
                genero=g,
                direccion_residencia=dr,
                persona=persona
            )
            list_info.append(persona_info)
    REP_INFO_PERSONA.objects.bulk_create(list_info)

def procesar_planilla(planilla:pd.DataFrame,dict_date:Dict):
    list_empresa = []
    list_contrato=[]
    for cod,name,dir,tel,nit,status,salario,empleado,puesto in zip(
            planilla['Codigo_Unico_Empresa'],
            planilla['Nombre_Empresa'],
            planilla['Direccion_Empresa'],
            planilla['Telefono_Empresa'],
            planilla['Nit_Empresa'],
            planilla['Condicion_laboral/estado'],
            planilla['Salario'],
            planilla['Empleado'],
            planilla['Puesto']
        ):
        emp = REP_EMPRESA.objects.filter(codigo=cod).first()
        persona = REP_PERSONA.objects.filter(dpi=empleado).first()
        if not emp:
            tmp = REP_EMPRESA(
                nombre_empresa=name,
                nit=nit,
                codigo=cod,
                direccion=dir,
                telefono=tel
            )
            list_empresa.append(tmp)
        else:
            tmp = emp
        if persona:
            try:
                dates = dict_date[empleado]
                if dates:
                    if len(dates) == 2:
                        valid = REP_TRABAJO.objects.filter(
                            id_persona=persona,
                            id_empresa=tmp,
                            nombre_puesto=puesto
                        ).first()
                        if not valid:
                            contrato=REP_TRABAJO(
                                id_persona=persona,
                                id_empresa=tmp,
                                salario=salario,
                                fecha_inicial=dates[0],
                                fecha_final=dates[1],
                                status=status,
                                nombre_puesto=puesto
                            )
                            list_contrato.append(contrato)
            except:
                print("ERROR")
    REP_EMPRESA.objects.bulk_create(list_empresa)
    REP_TRABAJO.objects.bulk_create(list_contrato)

def procesar_vacaciones(vacaciones:pd.DataFrame):
    #DPI,INICIO_VAC,FIN_VAC,NO_CONTRATO
    list_vacaciones = []
    for dpi,inicio,fin,contrato in zip(
            vacaciones['DPI'],
            vacaciones['INICIO_VAC'],
            vacaciones['FIN_VAC'],
            vacaciones['NO_CONTRATO']
        ):
        persona = REP_PERSONA.objects.filter(dpi=dpi).first()
        contrato = REP_TRABAJO.objects.filter(id_trabajo=contrato).first()
        vac = REP_VACACIONES.objects.filter(
            persona=persona,
            contrato=contrato,
            fecha_inicio=inicio,
            fecha_fin=fin
        ).first()
        if persona and contrato and not vac:
            tmp = REP_VACACIONES(
                fecha_inicio=inicio,
                fecha_fin=fin,
                persona=persona,
                contrato=contrato
            )
            list_vacaciones.append(tmp)
    REP_VACACIONES.objects.bulk_create(list_vacaciones)

def procesar_data(
        vacaciones:pd.DataFrame,
        empleados:pd.DataFrame,
        info_empleado:pd.DataFrame,
        planilla:pd.DataFrame
        )->pd.DataFrame:
    #DPI,NIT,Telefono,Correo_Electronico_trabajo,Cedula_Orden,Cedula_Registro,Fecha_Inicial,Fecha_Final
    dict_date=procesar_empleado(empleados)
    procesar_info_empleados(info_empleado)
    procesar_planilla(planilla,dict_date)
    procesar_vacaciones(vacaciones)