from django.forms.models import model_to_dict
from products.models import Products
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from products.serializers import ProductsSerializer

#####DRF APIVIEW######
####1) get#######
# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#    instance= Products.objects.all().order_by("?").first()
#    data = {}
#    if instance:
#       # data = model_to_dict(instance, fields = ['id', 'title', 'price', 'sale_price'])
#       data = ProductsSerializer(instance).data

#    return Response(data)

######2) post#########
@api_view(["POST"])
def api_home(request, *args, **kwargs):
   serializer = ProductsSerializer(data = request.data)
   if serializer.is_valid(raise_exception =True):
      instance = serializer.save()
      print(serializer.data)
      return Response(serializer.data)
   return Response({"invalid": "not good data"})







#################using Jsonresponse###################
from django.http import JsonResponse, HttpResponse
import json
     #######1) get method######

# def api_home(request, *args, **kwargs):
#    model_data = Products.objects.all().order_by("?").first()
#    data = {}
#    if model_data:
#       data = model_to_dict(model_data, fields = ['id', 'title', 'price'])   
#    return JsonResponse(data)

      #### 2)post method####

# def api_home(request,*args,**kwargs):
#    data ={}
#    data = request.data
#    return JsonResponse(data)

  