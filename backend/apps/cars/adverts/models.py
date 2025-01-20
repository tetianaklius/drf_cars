import datetime
from django.db import models
from django.core import validators as v

from core.models import BaseModel
from apps.auth_user.user.models import UserModel
from apps.cars.categories.models import CarCategoryModel
from apps.cars.brand.models import BrandModel
from apps.cars.car_model.models import CarModelModel
from apps.cars.location_city.models import CityModel
from apps.cars.car_dealership.models import CarDealershipModel
from core.services.file_service import upload_adv_photo


class CarAdvertModel(BaseModel):
    class Meta:
        db_table = "adverts"

    car_dealership_id = models.ForeignKey(CarDealershipModel, default=-1, on_delete=models.CASCADE,
                                          related_name="adverts")
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="adverts")
    title = models.CharField(max_length=60, unique=True)
    location_city = models.ForeignKey(CityModel, on_delete=models.SET("WITHOUT_CITY"), related_name="adverts")
    category = models.ForeignKey(CarCategoryModel, on_delete=models.SET("WITHOUT_CATEGORY"), related_name="adverts")
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, related_name="adverts")
    car_model = models.ForeignKey(CarModelModel, on_delete=models.CASCADE, related_name="adverts")
    year = models.IntegerField(blank=False, null=False, validators=[v.MinValueValidator(1960),
                                                                    v.MaxValueValidator(datetime.datetime.now().year)])
    price = models.IntegerField(blank=False, null=False,
                                validators=[v.MinValueValidator(1000), v.MaxValueValidator(1000000)])
    description = models.TextField(blank=False, null=False,
                                   validators=[v.MinLengthValidator(100), v.MaxLengthValidator(6000)])
    photo = models.ImageField(upload_to=upload_adv_photo, blank=True)
