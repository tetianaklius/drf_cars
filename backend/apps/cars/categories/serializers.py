from rest_framework import serializers

from apps.cars.categories.models import CarCategoryModel


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCategoryModel
        fields = ("id", "name", "value", "updated_at", "created_at")
