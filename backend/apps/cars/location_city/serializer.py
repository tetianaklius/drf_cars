from rest_framework import serializers

from apps.cars.location_city.models import CityModel


class CityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        fields = ("id", "name", "value", "updated_at", "created_at")