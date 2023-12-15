from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import AddProduct
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import ItemSerializer

def show_page(request): 
    product = Product.objects.all()
    return render(request,'home.html',{'product':product})

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def product_list(request, pk):
    instance = Product.objects.get(pk=pk)
    serialized = ItemSerializer(instance)
    return Response({'data':serialized.data}, template_name='product.html')

