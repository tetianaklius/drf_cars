from django.db import models

from core.models import BaseModel


class CarCategoryModel(BaseModel):
    class Meta:
        db_table = "categories"

    name = models.CharField(max_length=20, blank=False)
    value = models.IntegerField(blank=False)

