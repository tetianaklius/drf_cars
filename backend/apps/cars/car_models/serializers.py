from rest_framework import serializers

from apps.cars.car_models.models import CarModelModel


class CarModelModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModelModel
        fields = ("id", "name", "value", "brand", "created_at", "updated_at")


