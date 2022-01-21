from rest_framework.response import Response
from rest_framework import status
from product.models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_products(request):
    products = Product.objects.all().order_by('price')
    # I didn't understand what do you mean by filter by user if you meant
    # that only retrive the products created by the authenticated user
    # the line below fetch this data 😉😉😉
    # products = Product.objects.filter(seller=request.user.id)
    ser_products = ProductSerializer(products, many=True)
    return Response(data=ser_products.data,
                    status=status.HTTP_200_OK)


@api_view(['GET'])
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    ser_product = ProductSerializer(product)
    return Response(data=ser_product.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_product(request):
    data = {
        'name': request.data.get('name'),
        'price': request.data.get('price'),
        'seller': request.user.id
    }
    ser_product = ProductSerializer(data=data)
    if ser_product.is_valid():
        ser_product.save()
        return Response(data=ser_product.data, status=status.HTTP_201_CREATED)
    return Response(data=ser_product.errors,
                    status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail_filtered_by_username(request, username):
    # username = request.data.get('name')
    # user_id = User.objects.get(username=username).id
    user_id = get_object_or_404(User, username=username).id
    products = Product.objects.filter(seller=user_id)
    ser_products = ProductSerializer(products, many=True)
    return Response(data=ser_products.data, status=status.HTTP_200_OK)
