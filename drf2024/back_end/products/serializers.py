from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.ModelSerializer):
   class Meta:
      model =Products
      fields = [
         'title',
         'content',
         'price',
         'sale_price'
      ]