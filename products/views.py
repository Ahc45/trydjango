from ast import Try
from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse, Http404
from .models import Product
from .forms import productForm, rawProductForm
# Create your views here.
def product_detail(request ,*args, **kwargs):
    obj = Product.objects.get(id=1)
    data= {
        "obj" : obj,
    }
    return render(request, "product/detail.html", data)

def product_create(request, *args, **kwargs):
    form = productForm(request.POST or None)
    if form.is_valid():
        form.save()
    data = {
        'form' : form
    }
    return render(request, "product/form.html",data)
def product_raw_create(request, *args, **kwargs):
    form = rawProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    data = {
        'form' : form
    }
    return render(request, "product/raw_form.html", data)
def product_edit(request,id):
    try:
        obj = Product.objects.get(id=id)
    except:
        raise Http404
    form = rawProductForm()

    data = {'obj': obj, 'form': form}
    return render(request, "product/raw_form.html", data)