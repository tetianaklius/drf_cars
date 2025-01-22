from django.db import models
from django.core import validators as v

from core.models import BaseModel
from apps.cars.location_city.models import CityModel


class CarDealershipModel(BaseModel):
    class Meta:
        db_table = "car_dealerships"

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, validators=[v.MaxLengthValidator(8000)])
    phone = models.CharField(blank=False, max_length=10)  # todo
    email = models.EmailField()  # todo
    dealership_city = models.ForeignKey(CityModel, blank=False, on_delete=models.SET("WITHOUT_CITY"), related_name="dealerships")
    street = models.CharField(blank=False, max_length=200)
    house = models.IntegerField(blank=False)
    add_address_info = models.CharField(blank=True, max_length=200)
