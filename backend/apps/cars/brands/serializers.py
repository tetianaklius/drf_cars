from rest_framework import serializers

from apps.cars.brands.models import BrandModel


class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = ("id", "name", "value", "category", "updated_at", "created_at")
