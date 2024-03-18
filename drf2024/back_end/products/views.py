from rest_framework import  authentication, generics,mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products
from api.mixins import StaffEdittorPermissionMixin, UserQuerySetMixin
from .serializers import ProductsSerializer
from django.shortcuts import get_object_or_404

####list apiview #####
#### post ####
class ProductListAPIView(generics.ListAPIView ):
   queryset = Products.objects.all()
   serializer_class = ProductsSerializer



#### get ####
class ProductListCreateAPIView( UserQuerySetMixin,StaffEdittorPermissionMixin, generics.ListCreateAPIView):
   queryset = Products.objects.all()
   serializer_class = ProductsSerializer

   def perform_create(self,serializer):
      # email = serializer.validated_data.pop('email') 
      # print(email)
      title = serializer.validated_data.get("title")
      serializer.save(user=self.request.user)
   # def get_queryset(self, *args, **kwargs):
   #    qs = super().get_queryset(*args, **kwargs)
   #    request = self.request
   #    user = request.user
   #    if not user.is_authenticated:
   #       return Products.objects.none()
   #    # print(request.user)
   #    return qs.filter(user=request.user)

# @api_view(['GET', 'POST'])
# def product_alt_view(request, pk=None, *args, **kwargs):
#    method = request.method

#    if method == "GET":
#       if pk is not None:
#          obj = get_object_or_404(Products, pk=pk)
#          data = ProductsSerializer(obj,many=False).data
#       queryset = Products.objects.all()
#       data = ProductsSerializer(queryset, many=True).data
#       return Response(data)
   
#    if method == "POST":
#       serializer = ProductsSerializer(data = request.data)
#       if serializer.is_valid(raise_exception= True):
#          title = serializer.validated_data.get("title")
#          serializer.save()
#          return Response(serializer.data)
#       return Response({"invalid":"not good data"})

###### post ####
# class ProductCreateAPIView(generics.CreateAPIView):
#    queryset = Products.objects.all()
#    serializer_class = ProductsSerializer

#    def perform_create(self, serializer):
#       title = serializer.validated_data.get("title")
#       serializer.save()

# ####### get ######
class ProductDetailAPIView(UserQuerySetMixin,StaffEdittorPermissionMixin, generics.RetrieveAPIView):
   queryset = Products.objects.all()
   serializer_class = ProductsSerializer 
 
class ProductUpdateAPIView(UserQuerySetMixin,StaffEdittorPermissionMixin, generics.UpdateAPIView):
   queryset = Products.objects.all()
   serializer_class = ProductsSerializer
   lookup_field = "pk"

   def perform_update(self, serializer):
      instance = serializer.save()
      if not instance.content:
         instance.cotent = instance.title

class ProductDeleteAPIView(StaffEdittorPermissionMixin, generics.DestroyAPIView):
   queryset = Products.objects.all()
   serializer_class = ProductsSerializer
   lookup_field = "pk"
 
   def perform_destroy(self, instance):
      return super().perform_destroy(instance)
####################### MIXINS ########################
   
class ProductMixinView(
   mixins.ListModelMixin,
   mixins.CreateModelMixin,
   mixins.RetrieveModelMixin,
   generics.GenericAPIView
):
   queryset = Products.objects.all()
   serializer_class = ProductsSerializer

   def get(self,request,*args,**kwargs):
      pk = kwargs.get("pk")
      if pk is not None:
         return self.retrieve(request,*args,**kwargs)
      return self.list(request, *args, **kwargs)
   
   def post(self,request, *args, **kwargs):
      return self.create(request, *args, **kwargs)