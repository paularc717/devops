from django.urls import path
from . import views
 
urlpatterns = [
    path('usuarios/', views.usuarios_list, name='usuarios_list'),
    path('insertar/', views.insertar, name='insertar'),
    path('buscar/<int:codigo>/', views.buscar, name='buscar'),
    path('modificar/<int:codigo>/', views.modificar, name='modificar'),
    path('eliminar/<int:codigo>/', views.eliminar, name='eliminar'),
]
