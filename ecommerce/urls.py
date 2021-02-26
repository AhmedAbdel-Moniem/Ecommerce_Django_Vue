from django.contrib import admin
from django.urls import path
from apps.core import views as coreviews
from apps.store import views as storeviews
from apps.cart import views as cartviews
from apps.store.api import api_add_to_cart as api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', coreviews.frontend, name='frontpage'),
    path('cart/', cartviews.cart_detail, name='cart'),
    path('contact/', coreviews.contact, name='contact'),
    path('about/', coreviews.about, name='about'),
    
    # api
    path('api/add_to_cart/', api_view, name='api_add_to_cart'),
    # store
    path('<slug:category_slug>/<slug:slug>/', storeviews.product_details, name='product_detail'),
    path('<slug:slug>/', storeviews.category_detail, name='category_detail'),
    
    
]
