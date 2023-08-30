from django.urls import path
from . import views

urlpatterns = [
    path('alumnos/nuevo/', views.alumno_nuevo, name='alumno_nuevo'),
    path('alumnos/lista/', views.alumno_lista, name='alumno_lista'),
]

