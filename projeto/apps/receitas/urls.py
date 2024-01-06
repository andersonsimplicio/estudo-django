from django.contrib import admin
from django.urls import path
from .import views 


urlpatterns = [
    path('',views.home,name='home'),
    path('receitas/<int:id>/details',views.recietas,name='receita'),
]
