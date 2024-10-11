from django.urls import path

from learnBasics.quieroAprender.views import index, learn_language

urlpatterns = [
    path('', index, name='home'),
    path('languages/', learn_language, name='languages'),
]