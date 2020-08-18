from django.shortcuts import render
from .models import Items


def item_list(request):
    context = {
        'items': Items.objects.all()
    }
    return render(request,'home-page.html', context)

def checkout(request):
    return render(request, 'checkout-page.html', {})

def products(request):
    return render(request, 'product-page.html', {})
# python manage.py 

def login(request):
    return render(request, 'login.html')