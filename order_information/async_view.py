from django.shortcuts import render,HttpResponse
from django.views.generic.base import View
from .models import *

import json
# Create your views here.
class OrderCustomer(View):
    def get(self,request):
        pk  = request.GET.get("pk")
        customer = Customer.objects.get(pk=pk)
        return HttpResponse(json.dumps({
            "c_contack": customer.c_contack,
            "c_email": customer.c_email,
        }),content_type="application/json")