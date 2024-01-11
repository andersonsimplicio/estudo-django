from django.contrib import admin
from django.urls import path
from .views  import home,receitas_view,categorias_view


app_name = 'apps.receitas'

urlpatterns = [
    path('',home,name='home'),
    path('receitas/categorias/<int:id>',categorias_view,name='categorias'),
    path('receitas/<int:id>/details',receitas_view,name='detalhes'),
]
