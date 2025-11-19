from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

dizionario = {
    "gennaio" : "siamo a gennaio",
    "febbraio" : "siamo a febbraio",
    "marzo" : "siamo a marzo",
    "aprile" : "siamo ad aprile",
    "maggio" : "siamo a maggio",
    "giugno" : "siamo a giugno",
    "luglio" : "siamo a luglio",
    "agosto" : "siamo ad agosto",
    "settembre" : "siamo a settembre",
    "ottobre" : "siamo a ottobre",
    "novembre" : "siamo a novembre",
    "dicembre" : "siamo a dicembre",
}

def paginaLista(request):
    listaMesi=list(dizionario.keys())
    listItems=""
    for mese in listaMesi:
        meseCapitalizzato=mese.capitalize()
        meseRedirect=reverse("usato-per-riderect",args=[mese])
        listItems+=f"<li><a href=\"{meseRedirect} \" /> {meseCapitalizzato}</li>"
    textToReturn=f"<ul>{listItems}</ul>"
    return HttpResponse(textToReturn)



def challengeDelMeseByNumber(request, mese):
    listaMesi = list(dizionario.keys())

    if mese > 12 or mese < 1:
        return HttpResponseNotFound("Mese non valido")

    redirectMese = listaMesi[mese - 1]
    redirectPath = reverse("usato-per-riderect",args=[redirectMese])
    return HttpResponseRedirect(redirectPath)


def challengeDelMese(request, mese):

    try:
        variabileTesto=dizionario[mese]
        '''textToSentInResponse=f"<h1>{variabileTesto}</h1>" '''
        textToSentInResponse=render_to_string("challenges/challenge.html")
        return HttpResponse(textToSentInResponse)
    except:
        return HttpResponseNotFound("<h1 style='color:red'>Mese non valido</h1>")
