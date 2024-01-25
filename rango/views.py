from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpRespone("Rango says hey there partner!")


