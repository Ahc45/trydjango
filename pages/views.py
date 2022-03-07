from django.shortcuts import render
from django.http import  HttpResponse
from products.models import Product
# Create your views here.
def home_view(request ,*args, **kwargs):
    obj = Product.objects.get(id=1)
    data= {
        "obj" : obj
    }
    return render(request, "product/detail.html", data)