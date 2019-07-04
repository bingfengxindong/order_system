from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    url(r"^adadd",csrf_exempt(ADAdd.as_view()),name="adadd"),
    url(r"^adedit",csrf_exempt(ADEdit.as_view()),name="adedit"),
]