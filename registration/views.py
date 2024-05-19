# request handler, like Node.JS controllers
from django.shortcuts import render
from django.http import HttpResponse

def get_stocks(request):
    return HttpResponse('hello world')