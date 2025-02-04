from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class ChatRoomModel(models.Model):
    class Meta:
        db_table = "chat_room"

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MessageModel(models.Model):
    class Meta:
        db_table = "chat_message"

    room = models.ForeignKey(ChatRoomModel, on_delete=models.CASCADE, related_name="messages")
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="messages")
    text = models.TextField()
