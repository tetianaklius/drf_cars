from rest_framework import serializers

from apps.cars.car_model.models import CarModelModel


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModelModel
        fields = ("id", "name", "value", "updated_at", "created_at")
