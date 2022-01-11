from django.urls import path
from .views import create_product, list_products, product_detail
urlpatterns = [
    path('list/', list_products, name='List products'),
    path('details/<int:id>', product_detail, name='product details'),
    path('create/', create_product, name='create'),
]
