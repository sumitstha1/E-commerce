from django.urls import path
from account.views import *
from product.views import *


urlpatterns = [
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path('logout/', logout_page, name='logout'),
    path('activate/<email_token>', activate_email, name="activate_email"),
    path('cart/', cart, name="cart"),
    path('add-to-cart/<uid>/', add_to_cart, name="add_to_cart"),
    path('esewa-request/<uid>/', esewa_payment, name="esewa_request"),
    path('esewa_cart', esewa_cart, name="esewa_cart"),
    path('remove-cart/<cart_item_uid>/', remove_cart, name="remove_cart"),
    path('remove-coupon/<cart_id>/', remove_coupon, name="remove_coupon"),
]
