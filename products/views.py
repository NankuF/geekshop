from django.shortcuts import render

from .models import Product, ProductCategory


def index(request):
    context = {
        "title": "Geekshop",
    }
    return render(request, "products/index.html", context)


def products(request, category_id=None):
    context = {'title': 'Products', 'categories': ProductCategory.objects.all()}
    if category_id:
        context['products'] = Product.objects.filter(category_id=category_id)
    else:
        context['products'] = Product.objects.all()
    return render(request, "products/products.html", context)
