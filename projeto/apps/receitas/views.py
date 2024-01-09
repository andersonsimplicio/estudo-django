from tkinter.messagebox import NO
from unicodedata import category
from xmlrpc.client import Boolean
from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http import Http404
from utils.receitas.factory import make_produto
from .models import Receita
from typing import Optional

def home(request):
    prosdutos = Receita.objects.filter(is_published=True)
    return render(request,'home/home.html',context={
        'produtos':prosdutos,
        },)


def receitas(request,id:int):
    receita = get_object_or_404(Receita.objects.filter(id=id,is_published=True))
    is_detalis:Boolean = True
    context={'produto': receita,
              'is_detalis':is_detalis
            }
    
    return render(request,'home/receita.html',
                  context=context)

def categorias(request,id):
    produtos= get_list_or_404(Receita.objects.filter(category__id=id,is_published=True))
    if produtos is not None:
        nome_categoria = produtos[0].category
    else:
        nome_categoria =""
    return render(request,'home/categoria.html',context={
        'produtos':produtos,
        'cat_name':f'{nome_categoria.name}-categoria' # type: ignore
        },)