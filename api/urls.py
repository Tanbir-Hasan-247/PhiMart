from django.urls import path, include
# from rest_framework.routers import SimpleRouter
# from rest_framework.routers import DefaultRouter
from product.views import CategoryViewSet, ProductImageViewSet, ProductViewSet, ReviewViewSet
from order.views import CartItemViewSet, CartViewSet, OrderViewSet
from rest_framework_nested import routers

# router = SimpleRouter()
router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('carts', CartViewSet, basename='cart')
router.register('products', ProductViewSet, basename='product')
router.register('orders', OrderViewSet, basename='order')

product_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
product_router.register('reviews', ReviewViewSet, basename='product-reviews')
product_router.register('images', ProductImageViewSet, basename='product-images')

cart_router = routers.NestedDefaultRouter(
    router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart-items')

# urlpatterns = router.urls + product_router.urls + cart_router.urls
urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(cart_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

# urlpatterns = [
#     path('', include(router.urls)),
# ]

# urlpatterns = [
#     path('products/', include('product.product_urls')),
#     path('categories/', include('product.category_urls')),
#     path('carts/', include('order.cart_urls')),
# ]