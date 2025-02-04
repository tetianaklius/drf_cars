from django.db import models

from core.models import BaseModel


class CityModel(BaseModel):
    class Meta:
        db_table = "cities"

    name = models.CharField(max_length=30, blank=False, unique=True)
    value = models.IntegerField(blank=False)
