from rest_framework import serializers

from apps.cars.brand.models import BrandModel


class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = ("id", "name", "value", "updated_at", "created_at")
