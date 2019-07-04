from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    url(r"^psadd",csrf_exempt(PSAdd.as_view()),name="psadd"),
    url(r"^psedit",csrf_exempt(PSEdit.as_view()),name="psedit"),
    url(r"^endps",csrf_exempt(EndPS.as_view()),name="endps"),
]