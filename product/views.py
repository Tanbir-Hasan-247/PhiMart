from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer
from django.db.models import Count
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

# Create your views here.

@api_view(['GET', 'POST'])
def view_product(request):
    if request.method == 'GET':
        product = Product.objects.select_related('category').all()
        serializer = ProductSerializer(product, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])
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


@api_view(['GET', 'POST'])
def view_category(request):
    if request.method == 'GET':
        categories = Category.objects.annotate(product_count=Count('products')).all()
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def view_specific_category(request, pk):
    category = get_object_or_404(Category, pk = pk)
    serializer = CategorySerializer(category, context={'request': request})
    return Response(serializer.data)