from django.contrib import admin
from django.urls import path
from .views  import (home,receitas,categorias)


app_name = 'apps.receitas'

urlpatterns = [
    path('',home,name='home'),
    path('receitas/categorias/<int:id>',categorias,name='categorias'),
    path('receitas/<int:id>/details',receitas,name='detalhes'),
]
