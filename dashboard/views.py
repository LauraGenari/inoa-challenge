# request handler, like Node.JS controllers
from django.shortcuts import render
from django.http import HttpResponse

def get_stocks(request):
    return render(request, 'stocks.html')

def get_gates(request):
    return render(request, 'gates.html')

def set_stocks_to_email(request):
    return render(request, 'email.html')