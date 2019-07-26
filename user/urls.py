from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    url(r"^login",csrf_exempt(Login.as_view()),name="login"),
    url(r"^logout",csrf_exempt(Logout.as_view()),name="logout"),
]