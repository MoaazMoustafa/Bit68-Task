from django.urls import path
from .views import create_product, list_products, product_detail, detail_filtered_by_username
urlpatterns = [
    path('list/', list_products, name='List products'),
    path('details/<int:id>', product_detail, name='product details'),
    path('details/search/name/<str:username>',
         detail_filtered_by_username, name='product details'),
    path('create/', create_product, name='create'),
]
