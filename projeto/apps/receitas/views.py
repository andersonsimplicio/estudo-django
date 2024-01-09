from xmlrpc.client import Boolean
from django.shortcuts import render
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
    receita = Receita.objects.filter(id=id,is_published=True).first()
    is_detalis:Boolean = True
    context={'produto': receita,
              'is_detalis':is_detalis
            }
    
    return render(request,'home/receita.html',
                  context=context)

def categorias(request,id):
    produtos:Optional[Receita] = Receita.objects.filter(category__id=id,is_published=True) # type: ignore
    
    if produtos is None:
        nome_categoria:Optional[str] =produtos.first().category.name  # type: ignore
    else:
        raise Http404('Não encotrada :)')

   
    return render(request,'home/categoria.html',context={
        'produtos':produtos,
        'cat_name':f'{nome_categoria}-categoria'
        },)