from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
    return render(request, 'index/index.html', {})

def about(request):
    return render(request, 'index/about.html', {})