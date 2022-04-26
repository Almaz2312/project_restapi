from rest_framework import serializers

from products.models import Product
from .models import Favourite


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'
        read_only_fields = ('created', 'updated', 'customer')
        extra_kwargs = {
            'product': {'required': True}
        }

        def create(self, validated_data):
            product = Product.objects.get(id=validated_data.get('product').id)
            # current_item = Basket.objects.filter(customer=self.request.user, product=product)
            favourite = Favourite.objects.create(**validated_data, total_price=total_price)
            return favourite
