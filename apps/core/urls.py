from django.urls import path
from . import views
from apps.store import views as storeviews

urlpatterns = [
    path('', views.frontend, name='frontpage'),
    path('contact/', views.contact, name='contact'),
    path('<slug:slug>', storeviews.product_details, name='product_detail')
]