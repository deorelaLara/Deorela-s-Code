from django.shortcuts import render
from django.http import HttpResponse
import django

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def deorela(request):
    return HttpResponse('Hello Deorela')

def Haru(request):
    return HttpResponse('Hello Haruchino')

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name":name.capitalize()
    })
