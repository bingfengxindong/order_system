from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import *
from .order_search import *

urlpatterns = [
    url(r"^orderadd",csrf_exempt(OrderAdd.as_view()),name="orderadd"),
    url(r"^orderlist",csrf_exempt(OrderList.as_view()),name="orderlist"),
    url(r"^orderdetail",csrf_exempt(OrderDetail.as_view()),name="orderdetail"),
    url(r"^orderedit",csrf_exempt(OrderEdit.as_view()),name="orderedit"),
    url(r"^endorder",csrf_exempt(EndOrder.as_view()),name="endorder"),

    # 订单搜索
    url(r"^orderpp",csrf_exempt(OrderPP.as_view()),name="orderpp"),
    url(r"^orderps",csrf_exempt(OrderPS.as_view()),name="orderps"),
    url(r"^ordero",csrf_exempt(OrderO.as_view()),name="ordero"),
    url(r"^orderend",csrf_exempt(OrderEnd.as_view()),name="orderend"),
]