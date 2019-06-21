from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import *
from .async_view import *
from .search_views import *

urlpatterns = [
    url(r"^orderlist$", csrf_exempt(Orderlist.as_view()),name="orderlist"),
    url(r"^orderdetail$", csrf_exempt(OrderDetail.as_view()),name="orderdetail"),
    url(r"^orderedit$", csrf_exempt(OrderEdit.as_view()),name="orderedit"),
    url(r"^orderadd$", csrf_exempt(OrderAdd.as_view()),name="orderadd"),

    # 异步
    url(r"^ordercustomer$", csrf_exempt(OrderCustomer.as_view()),name="ordercustomer"),

    # 搜索
    url(r"^ppsearch$", csrf_exempt(PPSearch.as_view()),name="ppsearch"),
    url(r"^pssearch$", csrf_exempt(PSSearch.as_view()),name="pssearch"),
    url(r"^cpsearch$", csrf_exempt(CPSearch.as_view()),name="cpsearch"),
    url(r"^scsearch$", csrf_exempt(SCSearch.as_view()),name="scsearch"),
]