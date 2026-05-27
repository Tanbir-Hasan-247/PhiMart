from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer
from django.db.models import Count
from rest_framework import status
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework.views import APIView
# Create your views here.

# @api_view(['GET', 'POST'])
# def view_product(request):
#     if request.method == 'GET':
#         product = Product.objects.select_related('category').all()
#         serializer = ProductSerializer(product, many=True, context={'request': request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             print(serializer.validated_data)
#             serializer.save()
#             return Response(serializer.data, status=HTTP_201_CREATED)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ProductListCreateView(APIView):
    def get(self, request):
        product = Product.objects.select_related('category').all()
        serializer = ProductSerializer(product, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data, context={'request': request})
        # if serializer.is_valid():
        #     print(serializer.validated_data)
        #     serializer.save()
        #     return Response(serializer.data, status=HTTP_201_CREATED)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

# @api_view(['GET', 'PUT', 'DELETE'])
# def view_specific_product(request, id):

#     product = get_object_or_404(Product, pk=id)  # ✅ always available

#     if request.method == 'GET':
#         serializer = ProductSerializer(product, context={'request': request})
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ProductSerializer(
#             product,
#             data=request.data,
#             context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class SpecificProductView(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)  # ✅ always available
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)

    def put(self, request, id):
        product = get_object_or_404(Product, pk=id)  # ✅ always available
        serializer = ProductSerializer(
            product,
            data=request.data,
            context={'request': request}
        )
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)  # ✅ always available
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def view_category(request):
#     if request.method == 'GET':
#         categories = Category.objects.annotate(product_count=Count('products')).all()
#         serializer = CategorySerializer(categories, many=True, context={'request': request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CategorySerializer(data=request.data, context={'request': request})
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(serializer.data, status=HTTP_201_CREATED)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=HTTP_201_CREATED)

class CategoryListCreateView(APIView):
    def get(self, request):
        categories = Category.objects.annotate(product_count=Count('products')).all()
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data, context={'request': request})
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=HTTP_201_CREATED)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

# @api_view(['GET'])
# def view_specific_category(request, pk):
#     category = get_object_or_404(Category, pk = pk)
#     serializer = CategorySerializer(category, context={'request': request})
#     return Response(serializer.data)

class SpecificCategoryView(APIView):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk = pk)
        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        category = get_object_or_404(Category, pk = pk)
        serializer = CategorySerializer(category, data=request.data, context={'request': request})
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        category = get_object_or_404(Category, pk = pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)