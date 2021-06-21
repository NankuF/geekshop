from django.shortcuts import render

from .models import Product, ProductCategory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic.list import ListView


def index(request):
    context = {
        "title": "Geekshop",
    }
    return render(request, "products/index.html", context)


# def products(request, category_id=None, page=1):
#     context = {'title': 'Products', 'categories': ProductCategory.objects.all()}
#     products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
#
#     paginator = Paginator(products, 3)
#     try:
#         products_paginator = paginator.page(page)
#     except PageNotAnInteger:
#         products_paginator = paginator.page(1)
#     except EmptyPage:
#         products_paginator = paginator.page(paginator.num_pages)
#     context['products'] = products_paginator
#     return render(request, "products/products.html", context)


class ProductsListView(ListView):
    model = Product  # при использовании выдает ошибку UnorderedObjectListWarning: Pagination may yield inconsistent results
    queryset = Product.objects.all()
    template_name = 'products/products.html'
    paginate_by = 2
    context_object_name = 'product_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context.update({
            'title': 'Products',
            'categories': ProductCategory.objects.all(),
            'products': Product.objects.all()

        })
        return context


