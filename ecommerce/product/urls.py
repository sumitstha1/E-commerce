from django.urls import path
from product.views import *


urlpatterns = [
    path('<slug>/', get_product, name="get_product"),
    
]
