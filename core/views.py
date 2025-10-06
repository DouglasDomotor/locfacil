from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Bem vindo à minha primeira página!!!!</h1>')
