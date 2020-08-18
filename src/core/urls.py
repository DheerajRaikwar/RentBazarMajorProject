from django.urls import path
from .views import item_list, checkout, products, login


urlpatterns = [
    path('', item_list, name="list-of-items"),
    path('checkout/', checkout, name="checkout_page"),
    path('products/', products, name="show_products"),
    path('login/', login, name="login")
]

