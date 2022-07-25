from rest_framework import serializers

from store.models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
            "id",
            "name",
            "price",
            "description",
            "category",
        ]

