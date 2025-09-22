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
    path("<mese>",views.challengeDelMese)
]