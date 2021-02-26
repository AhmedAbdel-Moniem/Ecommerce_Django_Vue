import json
from django.http import JsonResponse, response
from .models import Product
from apps.cart.cart import Cart
from django.shortcuts import get_object_or_404

def api_add_to_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id   = request.POST.get('product_id')
    update       = request.POST.get('update')
    quantity     = request.POST.get('quantity')
 
    
    cart         = Cart(request)
    
    product      = get_object_or_404(Product, pk=product_id)
    
    if not update:
        cart.add(product=product, quantity=1, update_quantity=False)
    else:
        cart.add(product=product, quantity=quantity, update_quantity=True)
    return JsonResponse(jsonresponse)