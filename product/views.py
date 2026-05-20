from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.

@api_view()
def view_product(request):
    product = Product.objects.select_related('category').all()
    serializer = ProductSerializer(product, many=True, context={'request': request})
    return Response(serializer.data)

@api_view()
def view_specific_product(request, id):
    product = get_object_or_404(Product, pk = id)
    # product_dict = {
    #     'id': product.id,
    #     'name': product.name,
    #     'description': product.description,
    #     'price': product.price,
    #     'category': product.category.name,
    # }
    serializer = ProductSerializer(product, context={'request': request})
    return Response(serializer.data)


@api_view()
def view_category(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True, context={'request': request})
    return Response(serializer.data)

@api_view()
def view_specific_category(request, pk):
    category = get_object_or_404(Category, pk = pk)
    serializer = CategorySerializer(category, context={'request': request})
    return Response(serializer.data)