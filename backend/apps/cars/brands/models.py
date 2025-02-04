from django.db import models

from apps.cars.categories.models import CarCategoryModel
from core.models import BaseModel


class BrandModel(BaseModel):
    class Meta:
        db_table = "brands"

    name = models.CharField(max_length=30, blank=False, unique=True)
    value = models.IntegerField(blank=False)
    category = models.ForeignKey(CarCategoryModel, on_delete=models.SET_NULL, null=True, related_name="brands")
