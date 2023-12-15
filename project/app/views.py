from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request): 
    return HttpResponse('Hello World')

def show_page(request): 
    return render(request,'home.html')