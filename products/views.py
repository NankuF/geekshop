from django.shortcuts import render

from .models import Product, ProductCategory
from django.views.generic.list import ListView


def index(request):
    context = {
        "title": "Geekshop",
    }
    return render(request, "products/index.html", context)


class ProductsListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/products.html'
    paginate_by = 2
    context_object_name = 'product_list'
    ordering = ['-name']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        context.update({
            'title': 'Products',
            'categories': ProductCategory.objects.all(),
            'category_id': category_id,
            'filter_products_for_category_id': Product.objects.filter(category_id=category_id),
        })
        return context

