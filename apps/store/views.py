from django.shortcuts import render,get_object_or_404
from apps.core.views import Product
# Create your views here.
def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)
    