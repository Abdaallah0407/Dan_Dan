from django.shortcuts import get_object_or_404, render
from products.models import Product
from .models import Categori


def index(request):
    print('b')


def bycategory(request, categori_id):
    print('a')
    products = Product.objects.filter(categori=categori_id)
    categories = Categori.objects.all()

    context = {
        'products': products,
        'categories': categories
    }

    return render(request, 'products/products.html', context)
