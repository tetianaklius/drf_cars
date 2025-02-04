from django.db import models

from apps.cars.brands.models import BrandModel
from apps.cars.categories.models import CarCategoryModel
from core.models import BaseModel


class CarModelModel(BaseModel):
    class Meta:
        db_table = "car_models"

    name = models.CharField(max_length=35, blank=False, unique=True)
    value = models.IntegerField(blank=False)
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, related_name="car_models", null=True)
