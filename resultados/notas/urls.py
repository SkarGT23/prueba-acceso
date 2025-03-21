# notas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('notas/', views.notas_view, name='notas'),
    path('listar_notas/', views.listar_notas, name='listar_notas'),
]
