from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import *
from .async_view import *

urlpatterns = [
    url(r"^orderlist$", csrf_exempt(Orderlist.as_view()),name="orderlist"),
    url(r"^orderdetail$", csrf_exempt(OrderDetail.as_view()),name="orderdetail"),
    url(r"^orderedit$", csrf_exempt(OrderEdit.as_view()),name="orderedit"),
    url(r"^orderadd$", csrf_exempt(OrderAdd.as_view()),name="orderadd"),

    # 异步
    url(r"^ordercustomer$", csrf_exempt(OrderCustomer.as_view()),name="ordercustomer"),
]