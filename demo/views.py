from django.shortcuts import render,HttpResponse,redirect
from django.views.generic.base import View
from .models import *
# Create your views here.

class ALHandler(View):
    def get(self,request):
        als = A.objects.all()
        context = {
            "als":als,
        }
        return render(request=request,template_name="al.html",context=context)

class AHandler(View):
    def get(self,request):
        return render(request=request,template_name="a.html")

    def post(self,request):
        a = request.POST.get("a")
        b = request.POST.get("b")
        a1 = A.objects.create(a=a,b=b)
        return redirect("/demo/al")

class ADHandler(View):
    def get(self,request):
        pk = request.GET.get("pk")
        a = A.objects.get(pk=pk)
        context = {
            "a": a,
        }
        return render(request=request,template_name="ad.html",context=context)

class AEHandler(View):
    def get(self,request):
        pk = request.GET.get("pk")
        a = A.objects.get(pk=pk)
        a.ab_end = True
        a.save()
        return  redirect("/demo/ad?pk={}".format(pk))

class ABHandler(View):
    def get(self,request):
        context = {
            "a_pk": request.GET.get("pk"),
        }
        return render(request=request,template_name="ab.html",context=context)

    def post(self,request):
        a_pk = request.POST.get("a_pk")
        a = A.objects.get(pk=a_pk)
        c = request.POST.get("c")
        d = request.POST.get("d")
        b1 = B.objects.create(c=c,d=d)
        a.a_b.add(b1)
        return redirect("/demo/ad?pk={}".format(a_pk))

class BDHandler(View):
    def get(self,request):
        a_pk = request.GET.get("a_pk")
        pk = request.GET.get("pk")
        b = B.objects.get(pk=pk)
        context = {
            "a_pk": a_pk,
            "b": b,
        }
        return render(request=request,template_name="bd.html",context=context)

    def post(self,request):
        a_pk = request.POST.get("a_pk")
        pk = request.POST.get("pk")
        c = request.POST.get("c")
        d = request.POST.get("d")
        b = B.objects.get(pk=pk)
        b.c = c
        b.d = d
        b.save()
        return redirect("/demo/ad?pk={}".format(a_pk))

class BEHandler(View):
    def get(self,request):
        a_pk = request.GET.get("a_pk")
        pk = request.GET.get("pk")
        b = B.objects.get(pk=pk)
        b.b_end = True
        b.save()
        return redirect("/demo/ad?pk={}".format(a_pk))