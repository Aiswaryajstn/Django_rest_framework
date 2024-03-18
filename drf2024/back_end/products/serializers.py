from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Products
from .validators import validate_title
from api.serializers import UserPublicSerializer

class ProductsSerializer(serializers.ModelSerializer):
   owner = UserPublicSerializer(source= 'user',read_only = True)
   edit_url = serializers.SerializerMethodField(read_only=True)
   url = serializers.HyperlinkedIdentityField(
      view_name = 'product-detail',
      lookup_field = 'pk'
   )
   # email = serializers.EmailField(write_only=True  )
   class Meta:
      model =Products
      fields = [
         'owner',
         'url',
         'edit_url',
         # 'email',
         'pk',
         'title',
         'content',
         'price',
         'sale_price'
      ]
   title = serializers.CharField(validators=[validate_title])
   # def validate_title(self, value):
   #    qs = Products.objects.filter(title__iexact=value)
   #    if qs.exists():
   #       raise serializers.ValidationError(f"{value} is already a product name")
   #    return value
   # def create(self, validated_data):
   #    # return Products.objects.create(**validated_data)
   #    # email = validated_data.pop('email')
   #    obj = super().create(validated_data)
   #    # print(email, obj)
   #    return obj
   
   # def update(self, instance, validated_data):
   #    # instance.title = validated_data.get('title')
   #    # return instance
   #    email = validated_data.pop('eamil')
   #    return super().update(instance, validated_data)


   def get_edit_url(self, obj):
      request = self.context.get('request')
      if request is None:
         return None
      return reverse("product-edit", kwargs = {"pk": obj.pk}, request = request)