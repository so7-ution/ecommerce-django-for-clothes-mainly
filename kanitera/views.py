from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import category


def home(request):
    products = Product.objects.all().filter(is_available = True)
    product_count = products.count()

    context = {
            'products': products,
            'product_count': product_count,
    }
    return render(request, 'home.html', context)


def cat(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(category, slug=category_slug)
        products = Product.objects.filter(category = categories, is_available = True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available = True)
        product_count = products.count()

    context = {
            'products': products,
            'product_count': product_count,
    }
    return render(request, 'home.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
    }
    return render(request, 'product_detail.html', context)