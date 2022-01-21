# from django.contrib.auth.models import User
from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# I could return the username and email of the User by using nested serializers


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email')


# class ProductSerializer(serializers.ModelSerializer):
#     seller = UserSerializer()

#     class Meta:
#         model = Product
#         fields = '__all__'
