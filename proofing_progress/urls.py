from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    url(r"^ppadd",csrf_exempt(PPAdd.as_view()),name="ppadd"),
    url(r"^endpp",csrf_exempt(EndPP.as_view()),name="endpp"),
]