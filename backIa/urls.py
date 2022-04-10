from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers, serializers, viewsets
from apps.planilla import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path("hola/",views.transform_data),
    path("empleados/",views.Empleados.as_view()),
    path("vacaciones/",views.Vacaciones.as_view()),
    path("contrato/",views.Contratos.as_view()),
    path("empresas/",views.Empresas.as_view()),
    path("nan-empleado/",views.error_empleado),
    path("nan-planilla/",views.error_planilla),
    
]

