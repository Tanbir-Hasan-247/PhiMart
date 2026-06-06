from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Product, Review
from .serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from django.db.models import Count
from rest_framework import status
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework.views import APIView, Http404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import ProductFilter
# from rest_framework.pagination import PageNumberPagination
from .paginations import ProductPagination
# Create your views here.

# <--function based views-->
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

# <--class based views-->
# class ProductListCreateView(APIView):
#     def get(self, request):
#         product = Product.objects.select_related('category').all()
#         serializer = ProductSerializer(product, many=True, context={'request': request})
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ProductSerializer(data=request.data, context={'request': request})
#         # if serializer.is_valid():
#         #     print(serializer.validated_data)
#         #     serializer.save()
#         #     return Response(serializer.data, status=HTTP_201_CREATED)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=HTTP_201_CREATED)

# <--generic class based views-->
# class ProductListCreateView(ListCreateAPIView):
#     queryset = Product.objects.select_related('category').all()
#     serializer_class = ProductSerializer
    # def get_queryset(self):
    #     return Product.objects.select_related('category').all()
    
    # def get_serializer_class(self):
    #     return ProductSerializer
    
    # def get_serializer_context(self):
    #     return {'request': self.request}

# <--function based view-->
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

# <--class based view-->
# class SpecificProductView(APIView):
#     def get(self, request, id):
#         product = get_object_or_404(Product, pk=id)  # ✅ always available
#         serializer = ProductSerializer(product, context={'request': request})
#         return Response(serializer.data)

#     def put(self, request, id):
#         product = get_object_or_404(Product, pk=id)  # ✅ always available
#         serializer = ProductSerializer(
#             product,
#             data=request.data,
#             context={'request': request}
#         )
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(serializer.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def delete(self, request, id):
#         product = get_object_or_404(Product, pk=id)  # ✅ always available
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class SpecificProductView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.select_related('category').all()
#     serializer_class = ProductSerializer
#     lookup_field = 'id'
    
#     def delete(self, request, *args, **kwargs):
#         # product = get_object_or_404(Product, pk=kwargs['id'])
#         product = self.get_object()
#         if product.stock > 5:
#             return Response({'error': 'Cannot delete product with stock greater than 5.'}, status=status.HTTP_400_BAD_REQUEST)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class ProductViewSet(ModelViewSet):
    # queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['category_id', 'price']
    filterset_class = ProductFilter
    pagination_class = ProductPagination
    search_fields = ['name', 'description', 'category__name']
    ordering_fields = ['name', 'price', 'created_at']
    
    def get_queryset(self):
        product = Product.objects.select_related('category').all()
        
        category_id = self.request.query_params.get('category_id')
        if category_id:
            product = product.filter(category_id=category_id)
        return product
    
    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        if product.stock > 5:
            return Response({'error': 'Cannot delete product with stock greater than 5.'}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)

# <--function based view-->
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


# <--class based view-->
# class CategoryListCreateView(APIView):
#     def get(self, request):
#         categories = Category.objects.annotate(product_count=Count('products')).all()
#         serializer = CategorySerializer(categories, many=True, context={'request': request})
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CategorySerializer(data=request.data, context={'request': request})
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(serializer.data, status=HTTP_201_CREATED)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=HTTP_201_CREATED)


#<--generic class based view-->
# class CategoryListCreateView(ListCreateAPIView):
#     queryset = Category.objects.annotate(product_count=Count('products')).all()
#     serializer_class = CategorySerializer

# <--function based view-->
# @api_view(['GET'])
# def view_specific_category(request, pk):
#     category = get_object_or_404(Category, pk = pk)
#     serializer = CategorySerializer(category, context={'request': request})
#     return Response(serializer.data)

# <--class based view-->
# class SpecificCategoryView(APIView):
#     def get(self, request, pk):
#         category = get_object_or_404(Category, pk = pk)
#         serializer = CategorySerializer(category, context={'request': request})
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         category = get_object_or_404(Category, pk = pk)
#         serializer = CategorySerializer(category, data=request.data, context={'request': request})
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(serializer.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def delete(self, request, pk):
#         category = get_object_or_404(Category, pk = pk)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class SpecificCategoryView(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.annotate(product_count=Count('products')).all()
#     serializer_class = CategorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer
    

class ReviewViewSet(ModelViewSet):
    # queryset = Review.objects.select_related('product').all()
    serializer_class = ReviewSerializer
    
    def get_serializer_context(self):
        print(self.kwargs)
        return {'product_id': self.kwargs['product_id']}
    
    def get_queryset(self):
        if not Product.objects.filter(id=self.kwargs['product_id']).exists():
            raise Http404("Product with the given ID does not exist.")
        return Review.objects.select_related('product').filter(product_id=self.kwargs['product_id'])
    
    