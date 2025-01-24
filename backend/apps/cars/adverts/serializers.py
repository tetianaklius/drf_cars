from rest_framework import serializers

from apps.cars.adverts.models import CarAdvertModel
from core.checkers.profanity_checker import ProfanityChecker
from core.exceptions.profanity_check_exception import ProfanityCheckException


class AdvertPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAdvertModel
        fields = ("photo",)


class AdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAdvertModel
        fields = (
            "id", "user_id", "title", "car_dealership_id", "user_id", "location_city", "category", "brand", "car_model",
            "year", "price", "description", "profanity_edit_count", "updated_at", "created_at")
