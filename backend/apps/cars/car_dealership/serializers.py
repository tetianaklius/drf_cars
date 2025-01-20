from rest_framework import serializers

from apps.cars.adverts.serializers import AdvertSerializer
from apps.cars.car_dealership.models import CarDealershipModel


class CarDealershipSerializer(serializers.ModelSerializer):
    adverts = AdvertSerializer(many=True, read_only=True)

    class Meta:
        model = CarDealershipModel
        fields = (
            "id",
            "name",
            "description",
            "phone",
            "email",
            "dealership_city",
            "street",
            "house",
            "add_address_info",
            "adverts"
        )
        # depth = 1
