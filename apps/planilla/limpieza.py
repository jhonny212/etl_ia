import pandas as pd
import re
from datetime import datetime
from django.conf import settings
import numpy as np

def parsear_fecha(dt:pd.DataFrame,col):
    tmp = [re.sub(r'[\sA-Za-z]','',str(x)) for x in dt[col]]
    newrow = []
    for x in tmp:
        try:
            x=str(x).replace("/","-")
            try:
                fecha_dt = datetime.strptime(x, '%d-%m-%Y')
            except:
                try:
                    fecha_dt = datetime.strptime(x, '%m-%d-%Y')
                except:
                    try:
                        fecha_dt = datetime.strptime(x,'%Y-%m-%d')
                    except:
                        fecha_dt = None
            x = f"{fecha_dt.year}-{fecha_dt.month}-{fecha_dt.day}"
        except:
            x = None
        newrow.append(x)
    dt[col] = pd.Series(newrow)

def remover_guion(dt:pd.DataFrame,col):
    #tmp = [ if x is not None else None for x in dt[col] ]
    tmp = []
    for x in dt[col]:
        try:
            tmp.append(float(re.sub(r'[-_\sA-Za-z]','',str(x))))
        except:
            tmp.append(None)
    dt[col] = pd.Series(tmp)
    
    
    
def set_activo_inactivo(dt:pd.DataFrame)->pd.DataFrame:
    dt=dt.replace(to_replace =["A","a"],
                 value ="Activo")
    dt=dt.replace(to_replace =["I","i"],
                 value ="Inactivo")
    return dt

def set_genero(dt:pd.DataFrame)->pd.DataFrame:
    dt=dt.replace(to_replace =["M","m"],
                 value ="Masculino")
    dt=dt.replace(to_replace =["F","f"],
                 value ="Femenino")
    return dt

def limpiar_planilla(planilla:pd.DataFrame)->pd.DataFrame:
    cols_planilla = ["Telefono_Empresa","Nit_Empresa","Empleado"]
    nan_rows = planilla[planilla.isnull().any(1)]
    nan_rows.to_csv(settings.PLANILLA_NAN)
    for x in cols_planilla:
        remover_guion(planilla,x)
    remover_guion(planilla,'Salario')
    planilla=planilla.dropna()
    for x in cols_planilla:
        planilla[x] = planilla[x].round(0).astype(int)
    return set_activo_inactivo(planilla)

#limpieza de empleados
def limpiar_empleados(empleados:pd.DataFrame)->pd.DataFrame:
    nan_rows = empleados[empleados.isnull().any(1)]
    nan_rows.to_csv(settings.EMPLEADOS_NAN)
    if empleados.shape[0]<=0:
        return empleados
    cols_empleados = ['DPI', 'NIT','Telefono','Cedula_Orden','Cedula_Registro']
    for x in cols_empleados:
        remover_guion(empleados,x)
    parsear_fecha(empleados,'Fecha_Final')
    parsear_fecha(empleados,'Fecha_Inicial')
    empleados = empleados.dropna()
    for x in cols_empleados:
        empleados[x] = empleados[x].round(0).astype(int)
    #print(empleados)
    return set_genero(empleados)

def limpiar_vacaciones(vacaciones:pd.DataFrame)->pd.DataFrame:
    cols_empleados = ['DPI', 'NO_CONTRATO']
    for x in cols_empleados:
        remover_guion(vacaciones,x)
    parsear_fecha(vacaciones,'INICIO_VAC')
    parsear_fecha(vacaciones,'FIN_VAC')
    vacaciones=vacaciones.dropna()
    for x in cols_empleados:
        vacaciones[x] = vacaciones[x].round(0).astype(int)
    return vacaciones

def limpiar_info(info:pd.DataFrame)->pd.DataFrame:
    cols = ['DPI','Primer_Nombre','Segundo_Nombre',
        'Primer_Apellido','Segundo_Apellido']
    #info = info.dropna(subset=cols)
    if info.shape[0] <=0:
        return info
    remover_guion(info,'DPI')
    parsear_fecha(info,'Nacimiento')
    info = info.dropna(subset=cols)
    info['DPI'] = info['DPI'].round(0).astype(int)
    return info