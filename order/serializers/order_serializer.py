from rest_framework import serializers
from order.models import Order

from product.models import Product
from product.serializers.product_serializer import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)
    products_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True, write_only=True, source='product')
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total
    class Meta:
        model = Order
        fields = [ 'product', 'total', 'user', 'products_id' ]
        extra_kwargs = {'product': {'required': False}}

        def create(self, validated_data):
            product_data = validated_data.pop('products_id')
            user = validated_data.pop('user', None)
            order = Order.objects.create(**validated_data)
            
            for product in product_data:
                order.product.set(product)

            return order