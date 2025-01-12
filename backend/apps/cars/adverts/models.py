from django.db import models

from apps.auth_user.user.models import UserModel
from core.models import BaseModel


class CarAdvertModel(BaseModel):
    class Meta:
        db_table = "adverts"
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="adverts")
    title = models.CharField(max_length=60)
    # location_city_name =

    # category =
    # brand =
    # model =
    # year =
    # price =
    # description =

