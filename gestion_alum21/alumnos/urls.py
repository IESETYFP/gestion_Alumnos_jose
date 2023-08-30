from django.urls import path
from . import views

urlpatterns = [
    path('nuevo/', views.alumno_nuevo, name='alumno_nuevo'),
    path('lista/', views.alumno_lista, name='alumno_lista'),
]

