from django.shortcuts import render
from store.models import Product


def home(request):
    products = Product.objects.all().filter(is_available=True) #This is will fetch only the products which are available.
    context = {
        'products': products
    }
    return render(request, 'home.html', context)

