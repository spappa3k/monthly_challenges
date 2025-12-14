from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

dizionario = {
    "january": "Run for 20 minutes every day to boost your stamina and mood.",
    "february": "Drink at least 2 liters of water every day throughout the month.",
    "march": "Add two servings of fresh vegetables to your meals every day.",
    "april": "Complete a total of 30 km of walking by the end of the month.",
    "may": "Do 15 minutes of stretching every morning to improve flexibility.",
    "june": "Try a new outdoor activity (cycling, hiking, swimming) at least twice a week.",
    "july": "Cut added sugars and replace them with fresh fruit.",
    "august": "Meditate for 10 minutes every day to improve focus and relaxation.",
    "september": "Walk at least 8,000 steps per day.",
    "october": "Avoid processed foods for the whole month and choose fresh, whole foods instead.",
    "november": "Do strength training three times a week with bodyweight exercises (squats, planks, push-ups).",
    "december": None,
}

def index(request):
    mesi=list(dizionario.keys())
    return render(request,"challenges/index.html",{"mesi":mesi})


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
        '''textToSentInResponse=f"<h1>{variabileTesto}</h1>" 
        textToSentInResponse=render_to_string("challenges/challenge.html") 
        return HttpResponse(textToSentInResponse) '''
        
        return render(request, "challenges/challenge.html",{"title":mese, "text":variabileTesto})
    except:
        return HttpResponseNotFound("<h1 style='color:red'>Mese non valido</h1>")
