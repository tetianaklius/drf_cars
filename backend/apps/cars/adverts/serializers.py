from rest_framework import serializers

from apps.cars.adverts.models import CarAdvertModel


class AdvertPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAdvertModel
        fields = ("photo",)


class AdvertSerializer(serializers.ModelSerializer):
    # photo = AdvertPhotoSerializer()
    class Meta:
        model = CarAdvertModel
        fields = (
            "id", "user_id", "title", "car_dealership_id", "user_id", "location_city", "category", "brand", "car_model",
            "year", "price", "description", "updated_at", "created_at")

    # def create(self, validated_data):
    #     user_id = self.request.user.id
    # user_id = serializers.ReadOnlyField(source="user.id")
