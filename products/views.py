from django.shortcuts import get_object_or_404, render

from .models import Product
from categories.models import Categori

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):

    products = Product.objects.order_by('-list_date').filter(is_published=True)
    categories = Categori.objects.all()
    # for i in categories:
    #     print(i.title)
    #     print('a')
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products': paged_products,
        'categories': categories
    }

    return render(request, 'products/products.html', context)


def product(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    context = {
        'product': product
    }

    return render(request, 'products/product.html', context)


def search(request):

    return render(request, 'products/search.html')
