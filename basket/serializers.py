from rest_framework import serializers
from rest_framework.exceptions import ValidationError, NotAcceptable
from django.contrib.auth import get_user_model

from products.models import Product
from .models import Basket

User = get_user_model()


# class BasketListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Basket
#         fields = ('')


class BasketSerializer(serializers.ModelSerializer):
    total_sum = serializers.DecimalField(read_only=True, max_digits=20, decimal_places=2)
    class Meta:
        model = Basket
        fields = '__all__'
        read_only_fields = ('customer', 'total_price', 'total_sum')
        extra_kwargs = {
            'total_quantity': {'required': True}
        }


    # def validate_product(self, value):
    #     basket = Basket.objects.filter(name=value)
    #     if not basket.product.name:
    #         raise ValidationError('Product already exists')
    #     return value

    def create(self, validated_data):
        total_quantity = validated_data.get('total_quantity')
        product = Product.objects.get(id=validated_data.get('product').id)
        total_price = product.price * total_quantity
        # current_item = Basket.objects.filter(customer=self.request.user, product=product)
        basket = Basket.objects.create(**validated_data, total_price=total_price)
        return basket

    # def update