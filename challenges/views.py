from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

'''
def gennaioFunzione(request):
      return HttpResponse("siamo su gennaio")

def febbraioFunzione(request):
      return HttpResponse("siamo su febbraio")
'''

def challengeDelMese(request, mese):
    variabileTesto=None

    if mese == "gennaio":
        variabileTesto="Siamo a Gennaio"
    elif mese == "febbraio":
        variabileTesto="Siamo a Febbraio"
    elif mese =="marzo":
        variabileTesto="Siamo a Marzo"
    else:
        return HttpResponseNotFound("Questo mese non esiste")
    return HttpResponse(variabileTesto)