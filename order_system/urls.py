from django.contrib import admin
from django.conf.urls import url,include
from django.views.static import serve
from .settings import STATICFILES_DIRS,MEDIA_ROOT
from order_system import view

import os
import order
import proofing_progress
import production_schedule
import quotation
import accounting_documents
import user


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^order/', include(("order.urls","order"),namespace="order")),
    url(r'^pp/', include(("proofing_progress.urls","pp"),namespace="pp")),
    url(r'^ps/', include(("production_schedule.urls","ps"),namespace="ps")),
    url(r'^q/', include(("quotation.urls","q"),namespace="q")),
    url(r'^ad/', include(("accounting_documents.urls","ad"),namespace="ad")),
    url(r'^user/', include(("user.urls","user"),namespace="user")),
    url(r"^static/(?P<path>.*)",serve,{"document_root": STATICFILES_DIRS[0]}, name="static"),
    url(r"^media/(?P<path>.*)",serve,{"document_root":MEDIA_ROOT},name="media"),
]

handler403 = view.page_permission_denied
handler404 = view.page_not_found
handler500 = view.page_inter_error