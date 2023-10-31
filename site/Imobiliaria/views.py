from django.http import HttpResponse
from django.shortcuts import render



        

        

def index(request):
    return HttpResponse('')

def imoveis(request):
    imoveis = imoveis.objects.all()
    return render(request, 'imoveis.html', {'imoveis': imoveis})
