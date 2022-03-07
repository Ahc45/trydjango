"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view
from products.views import product_detail, product_create, product_raw_create, product_edit

urlpatterns = [
    path('', home_view, name="home"),
    path('product', product_detail),
    path('product/create', product_create),
    path('product/raw_create', product_raw_create),
    path('product/edit/<int:id>/', product_edit,name="product"),
    path('admin/', admin.site.urls),
]
