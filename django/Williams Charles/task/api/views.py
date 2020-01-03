from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def apiView(request):
    return HttpResponse("<h1>WELCOME</h1>")
