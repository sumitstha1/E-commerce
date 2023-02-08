from django.shortcuts import render, redirect
from .models import *
from account.models import *
from django.db.models import Q

# Create your views here.


def get_product(request, slug):
    try:
        product = Product.objects.get(slug = slug)
        context = {
            'product': product
        }

        if request.GET.get('size'):
            size = request.GET.get('size')
            context['selected_size'] = size

        return render(request, 'product/product.html', context)
    except Exception as e:
        print(e)


def get_category_product(request, slug):
    try:
        categtory_product = Category.objects.get(slug = slug)

        context = {
            'categories': categtory_product
        }

        return render(request, 'product/category_product.html', context)
    except Exception as e:
        print(e)

def get_brand_product(request, slug):
    try:
        brand_product = Brands.objects.get(slug = slug)

        context = {
            'brands': brand_product
        }

        return render(request, 'product/brand_product.html', context)
    except Exception as e:
        print(e)