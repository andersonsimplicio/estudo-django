from django.shortcuts import render



def home(request):
    return render(request,'home/home.html',context={'name':'Anderson Simplicio','title':'HOME'},)