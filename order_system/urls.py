from django.contrib import admin
from django.conf.urls import url,include
from django.views.static import serve
from .settings import STATICFILES_DIRS,MEDIA_ROOT

import os
import order_information

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^order/', include(("order_information.urls","order"),namespace="order")),
    url(r'^demo/', include(("demo.urls","order"),namespace="demo")),
    url(r"^static/(?P<path>.*)",serve,{"document_root": STATICFILES_DIRS[0]}, name="static"),
    url(r"^media/(?P<path>.*)",serve,{"document_root":MEDIA_ROOT},name="media"),
]