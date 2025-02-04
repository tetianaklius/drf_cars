from rest_framework import serializers

from apps.posts.models import PostModel


class PostCreateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = (
            "id",
            "is_visible",
            "is_active",
            "user_id",
            "title",
            "text",
            "label",
            "profanity_edit_count",
            "created_at",
            "updated_at",
        )
        read_only_fields = ["id", "is_visible", "is_active", "user_id", "profanity_edit_count", "created_at", "updated_at"]


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = (
            "title",
            "text",
            "label",
        )

    read_only_fields = ["id", "is_active", "user_id", "profanity_edit_count", "created_at", "updated_at"]
