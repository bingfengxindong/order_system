from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    url(r"^al$", csrf_exempt(ALHandler.as_view()),name="al"),
    url(r"^a$", csrf_exempt(AHandler.as_view()),name="a"),
    url(r"^ad$", csrf_exempt(ADHandler.as_view()),name="ad"),
    url(r"^ae$", csrf_exempt(AEHandler.as_view()),name="ae"),

    url(r"^ab$", csrf_exempt(ABHandler.as_view()),name="ab"),
    url(r"^bd$", csrf_exempt(BDHandler.as_view()),name="bd"),
    url(r"^be$", csrf_exempt(BEHandler.as_view()),name="be"),
]