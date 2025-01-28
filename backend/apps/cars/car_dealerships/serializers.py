from rest_framework import serializers

from apps.cars.adverts.serializers import AdvertSerializer
from apps.cars.car_dealerships.models import CarDealershipModel


class CarDealershipSerializer(serializers.ModelSerializer):
    adverts = AdvertSerializer(many=True, read_only=True)

    class Meta:
        model = CarDealershipModel
        fields = (
            # "id",
            "is_visible",
            "is_active",
            "name",
            "description",
            "phone",
            "email",
            "dealership_city",
            "street",
            "house",
            "additional_address_info",
            "user_id",
            "adverts"
        )
        read_only_fields = ["is_visible", "is_active", "user_id", "profanity_edit_count"]
        # write_only_fields = ["profanity_edit_count"]
        # extra_kwargs = {"is_active": {'write_only': True, }}
        # depth = 1
