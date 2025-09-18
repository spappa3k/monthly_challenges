from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def gennaioFunzione(request):
      return HttpResponse("siamo su gennaio")

def febbraioFunzione(request):
      return HttpResponse("siamo su febbraio")
