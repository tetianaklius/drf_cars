from rest_framework import serializers

from apps.profile_staff.models import ProfileStaffModel


class ProfileStaffModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileStaffModel
        fields = ("id", "is_active", "updated_at", "created_at", "car_dealership_id", "role",
                  "work_experience", "work_phone", "work_email")
        read_only_fields = ("id", "is_active", "updated_at", "created_at", "user_id")
