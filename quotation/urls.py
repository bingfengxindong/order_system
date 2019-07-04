from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    url(r"^qadd",csrf_exempt(QAdd.as_view()),name="qadd"),
    url(r"^qedit",csrf_exempt(QEdit.as_view()),name="qedit"),
]