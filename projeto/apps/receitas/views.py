from xmlrpc.client import Boolean
from django.shortcuts import render
from utils.receitas.factory import make_produto
from .models import Receita

def home(request):
    return render(request,'home/home.html',context={
        'produtos':Receita.objects.all(),
        },)


def receitas(request,id:int):
    receita = Receita.objects.filter(id=id).first()
    is_detalis:Boolean = True
    context={'produto': receita,
              'is_detalis':is_detalis
            }
    
    return render(request,'home/receita.html',
                  context=context)
def categorias(request,id):
    produtos = Receita.objects.filter(category__id=id)
    return render(request,'home/home.html',context={
        'produtos':produtos,
        },)