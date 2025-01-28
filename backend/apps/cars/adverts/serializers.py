from rest_framework import serializers

from apps.cars.adverts.models import CarAdvertModel
from apps.cars.brands.serializers import BrandModelSerializer
from apps.cars.car_models.serializers import CarModelModelSerializer
from apps.cars.categories.serializers import CategoryModelSerializer
from apps.cars.location_city.serializer import CityModelSerializer
from core.services.currency_service import get_calculated_prices, get_currency_points, point_is_actual


class AdvertPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAdvertModel
        fields = ("photo",)


class AdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAdvertModel
        fields = (
            "id", "user_id", "title", "car_dealership_id", "location_city", "category", "brand", "car_model",
            "year", "price", "description", "profanity_edit_count", "updated_at", "created_at", "region", "mileage",
            "gearbox", "fuel", "expired_at", "currency")
        read_only_fields = ("id", "user_id", "price_init", "profanity_edit_count", "expired_at")
        extra_kwargs = {'is_active': {'write_only': True, }}

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs["price_init"] = self.context["price_init"]
        return attrs


class AdvertUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAdvertModel
        fields = (
            "title", "location_city", "price", "description", "profanity_edit_count", "gearbox", "fuel", "expired_at")
        read_only_fields = ["expired_at", "profanity_edit_count"]
        extra_kwargs = {"is_active": {'write_only': True, }}


class AdvertListAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAdvertModel
        fields = (
            "title", "car_dealership_id", "location_city", "brand", "car_model",
            "year", "price", "description"
        )


class AdvertListByUserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAdvertModel
        fields = (
            "id", "user_id", "title", "car_dealership_id", "location_city", "category", "brand", "car_model",
            "year", "price", "description", "updated_at", "created_at")


class AdvertDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAdvertModel

        fields = ("id", "user_id", "title", "car_dealership_id", "location_city", "category", "brand", "car_model",
                  "year", "price", "description", "updated_at", "created_at")

    def to_representation(self, instance):
        obj = super(AdvertDetailsSerializer, self).to_representation(instance)

        if hasattr(instance, "counter"):
            obj["counter"] = instance.counter
        if hasattr(instance, "avg_prices"):
            obj["avg_prices"] = instance.avg_prices
        obj["calc_prices"] = get_calculated_prices(instance.price, instance.currency.id)
        obj["currency_points"] = get_currency_points()
        obj["point_is_actual"] = point_is_actual()

        return obj
