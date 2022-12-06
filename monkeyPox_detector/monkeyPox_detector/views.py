from django.http import HttpRequest
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def quiz(request):
    return render(request,'quiz.html')

def test(request):
    return render(request,'test.html')
