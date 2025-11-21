from django.urls import path
from . import views

'we are doing a url config'

'''
urlpatterns = [
    path("gennaio",views.gennaioFunzione),
    path("febbraio",views.febbraioFunzione)
]
'''

urlpatterns = [
    path("",views.index),
    path("<int:mese>",views.challengeDelMeseByNumber),
    path("<str:mese>",views.challengeDelMese, name="usato-per-riderect")
]