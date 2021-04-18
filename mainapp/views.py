from django.shortcuts import render
from mainapp.models import ProductCategory, Product

from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page


# Create your views here.
def index(request):
    context = {
        'title': 'geekShop',
    }
    return render(request, 'mainapp/index.html', context)


# def products(request, id=None):
#     context = {
#         'title': 'geekShop - Каталог',
#         'products': Product.objects.all(),
#         'categories': ProductCategory.objects.all(),
#     }
#     return render(request, 'mainapp/products.html', context)

def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    per_page = 3
    paginator = Paginator(products.order_by('-price'), per_page)
    products_paginator = paginator.page(page)
    context = {'categories': ProductCategory.get_all(), 'products': products_paginator}
    return render(request, 'mainapp/products.html', context)
