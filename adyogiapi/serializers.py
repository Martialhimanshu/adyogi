from rest_framework.serializers import ModelSerializer

from adyogiapi.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
