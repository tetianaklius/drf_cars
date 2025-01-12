from rest_framework import serializers

from apps.cars.adverts.models import CarAdvertModel


class AdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAdvertModel
        fields = ("id", "user_id", "title", "updated_at", "created_at")

    # def create(self, validated_data):
    #     user_id = self.request.user.id
    # user_id = serializers.ReadOnlyField(source="user.id")

