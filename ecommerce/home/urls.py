from django.urls import path
from home.views import *
from product.views import *
from account.views import *


urlpatterns = [
    path('', index, name='index'),
    path('category/', get_category, name='get_category'),
    path('brand/', get_brand, name='get_brand'),
    path('category/<slug>/', get_category_product, name="get_category_product"),
    path('brand/<slug>/', get_brand_product, name="get_brand_product"),
    path('addquantity/', add_quantity),
    path('subquantity/', sub_quantity),
]
