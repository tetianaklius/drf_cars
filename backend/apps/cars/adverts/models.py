import datetime
from django.db import models
from django.core import validators as v

from apps.currency.models import CurrencyModel
from core.models import BaseModel
from apps.auth_user.user.models import UserModel
from apps.cars.categories.models import CarCategoryModel
from apps.cars.brands.models import BrandModel
from apps.cars.car_models.models import CarModelModel
from apps.cars.location_city.models import CityModel
from apps.cars.car_dealerships.models import CarDealershipModel
from core.services.file_service import upload_adv_photo


class CarAdvertModel(BaseModel):
    class Meta:
        db_table = "adverts"

    is_active = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    car_dealership_id = models.ForeignKey(CarDealershipModel, default=-1, on_delete=models.CASCADE,
                                          related_name="adverts")
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="adverts")
    title = models.CharField(max_length=60, unique=True)
    location_city = models.ForeignKey(CityModel, on_delete=models.SET("WITHOUT_CITY"), related_name="adverts")
    region = models.IntegerField(null=False)  # todo
    category = models.ForeignKey(CarCategoryModel, on_delete=models.SET("WITHOUT_CATEGORY"), related_name="adverts")
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, related_name="adverts")
    car_model = models.ForeignKey(CarModelModel, on_delete=models.CASCADE, related_name="adverts")
    year = models.IntegerField(blank=False, null=False, validators=[v.MinValueValidator(1960),
                                                                    v.MaxValueValidator(datetime.datetime.now().year)])
    price = models.IntegerField(blank=False, null=False,
                                validators=[v.MinValueValidator(1000), v.MaxValueValidator(1000000)])
    price_init = models.IntegerField(validators=[v.MinValueValidator(1000), v.MaxValueValidator(1000000)])  # todo
    currency = models.ForeignKey(CurrencyModel, on_delete=models.SET_DEFAULT, default=1, related_name="adverts")
    mileage = models.FloatField()  # todo validator
    gearbox = models.IntegerField(null=True)  # todo FK
    fuel = models.IntegerField(null=True)  # todo FK
    description = models.TextField(blank=False, null=False,
                                   validators=[v.MinLengthValidator(100), v.MaxLengthValidator(6000)])
    photo = models.ImageField(upload_to=upload_adv_photo, blank=True)
    expired_at = models.DateTimeField(null=True)  # todo validator
    profanity_edit_count = models.IntegerField(default=0, validators=[v.MinValueValidator(0)])
