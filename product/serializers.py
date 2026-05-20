from rest_framework import serializers
from decimal import Decimal
from .models import Category

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(allow_blank=True, required=False)

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    # price = serializers.DecimalField(max_digits=10, decimal_places=2)
    unit_price = serializers.DecimalField(max_digits=10, decimal_places=2, source='price')
    # category = serializers.StringRelatedField()
    # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    # category = CategorySerializer()
    
    category = serializers.HyperlinkedRelatedField(
        queryset=Category.objects.all(),
        view_name='view_specific_category'
    )
    price_with_tax = serializers.SerializerMethodField(method_name='get_price_with_tax')

    def get_price_with_tax(self, obj):
        # Example tax rate (15%)
        return round(obj.price * Decimal('1.15'), 2)