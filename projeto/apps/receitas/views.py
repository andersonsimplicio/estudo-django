from django.shortcuts import render
from utils.receitas.factory import make_produto


def home(request):
    return render(request,'home/home.html',context={
        'name':'Anderson Simplicio',
        'produtos': [make_produto() for _ in range(10)],
        },)


def recietas(request,id:int):
    return render(request,'home/receita.html',
                  context={'produto': make_produto(),
                           'is_detalis':True
                           })