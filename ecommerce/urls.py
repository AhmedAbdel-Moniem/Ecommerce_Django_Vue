from django.contrib import admin
from django.urls import path
from apps.core import views as coreviews
from apps.store import views as storeviews
from apps.cart.views import cart


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', coreviews.frontend, name='frontpage'),
    path('contact/', coreviews.contact, name='contact'),
    path('about/', coreviews.about, name='about'),
    
    path('<slug:category_slug>/<slug:slug>/', storeviews.product_details, name='product_detail'),
    path('<slug:slug>/', storeviews.category_detail, name='category_detail'),
    
    path('cart/', cart, name='cart'),
]
