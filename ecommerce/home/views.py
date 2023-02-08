from django.shortcuts import render
from product.models import *

# Create your views here.
def index(request):
    context = {'products' : Product.objects.all()}
    return render(request, 'home/index.html', context)

def get_category(request):
    category = Category.objects.all()
    context = {
        'categories': category
    }

    return render(request, 'home/category.html', context)

def get_brand(request):
    brand = Brands.objects.all()
    context = {
        'brands': brand
    }

    return render(request, 'home/brand.html', context)



