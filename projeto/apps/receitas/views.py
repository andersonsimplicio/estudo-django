from django.shortcuts import render



def home(request):
    return render(request,'global/home/home.html',context={'name':'Anderson'},)