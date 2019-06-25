from django.db import models

# Create your models here.
class A(models.Model):
    a = models.CharField(max_length=100,null=True,blank=True)
    b = models.CharField(max_length=100,null=True,blank=True)
    a_b = models.ManyToManyField("B",blank=True,null=True)
    a_c = models.ForeignKey("C",on_delete=models.CASCADE,blank=True,null=True)
    ab_end = models.BooleanField(default=False)

class B(models.Model):
    c = models.CharField(max_length=100,null=True,blank=True)
    d = models.CharField(max_length=100,null=True,blank=True)
    b_end = models.BooleanField(default=False)

class C(models.Model):
    e = models.CharField(max_length=100,null=True,blank=True)
    f = models.CharField(max_length=100,null=True,blank=True)