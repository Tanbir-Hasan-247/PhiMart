from rest_framework import serializers

from product.models import Product
from .models import Cart, CartItem

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        # model = CartItem.product.field.related_model
        model = Product
        fields = ['id', 'name', 'price']

class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    
    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity']
        
    def validate_product_id(self, value):
        if not Product.objects.filter(id=value).exists():
            raise serializers.ValidationError('No product with the given ID was found.')
        return value
    
    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']
        
        try:
            cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(cart_id=cart_id, **self.validated_data)
        
        return self.instance

class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']

class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer(read_only=True)
    total_price = serializers.SerializerMethodField(method_name='get_total_price')

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']
        
    def get_total_price(self, cart_item: CartItem):
        return cart_item.product.price * cart_item.quantity

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='get_total_price')

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'items', 'total_price']
        
    def get_total_price(self, cart: Cart):
        return sum(item.product.price * item.quantity for item in cart.items.all())