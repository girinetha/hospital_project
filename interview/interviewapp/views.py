from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.
def display(request):
    return HttpResponse("<h1>successfully loaded</h1>")