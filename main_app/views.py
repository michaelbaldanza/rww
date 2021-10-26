from django.shortcuts import render
from django.http import HttpResponse

def about(request):
  return HttpResponse('<h1>about</h1>')

def home(request):
  return render(request, 'index.html')