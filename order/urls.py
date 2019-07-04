from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    url(r"^orderadd",csrf_exempt(OrderAdd.as_view()),name="orderadd"),
    url(r"^orderlist",csrf_exempt(OrderList.as_view()),name="orderlist"),
    url(r"^orderdetail",csrf_exempt(OrderDetail.as_view()),name="orderdetail"),
    url(r"^orderedit",csrf_exempt(OrderEdit.as_view()),name="orderedit"),
    url(r"^endorder",csrf_exempt(EndOrder.as_view()),name="endorder"),
]