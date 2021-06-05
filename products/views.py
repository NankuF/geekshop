from django.shortcuts import render

from .models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {
        "title": "Geekshop",
    }
    return render(request, "products/index.html", context)


def products(request):
    products = Product.objects.all()
    category = ProductCategory.objects.all()
    context = {
        "title": "Products",
        'products': products,
        'category': category,
    }
    return render(request, "products/products.html", context=context)

# def products(request, pk=None):
#     if pk:
#         products = Product.objects.filter(id=pk)
#     else:
#         products = Product.objects.all()
#     context = {
#         "title": "Products",
#         'products': products
#     }
#     return render(request, "products/products.html", context=context)
