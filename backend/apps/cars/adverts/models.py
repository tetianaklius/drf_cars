from django.db import models

from apps.auth_user.user.models import UserModel
from core.models import BaseModel
from core.services.file_service import upload_adv_photo


class CarAdvertModel(BaseModel):
    class Meta:
        db_table = "adverts"
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="adverts")
    title = models.CharField(max_length=60)
    # location_city_name =

    photo = models.ImageField(upload_to=upload_adv_photo, blank=True)
    # category =
    # brand =
    # model =
    # year =
    # price =
    # description =

