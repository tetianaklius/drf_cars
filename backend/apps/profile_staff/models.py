from apps.cars.car_dealerships.models import CarDealershipModel
from core.models import BaseModel
from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class StaffChoicesModel(models.TextChoices):
    ADMIN = "Admin"
    MANAGER = "Manager"
    SALES = "Sales"
    MECHANIC = "Mechanic"


class ProfileStaffModel(BaseModel):
    class Meta:
        db_table = "profile_staff"

    is_active = models.BooleanField(default=False)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="profile_staff")
    car_dealership_id = models.ForeignKey(CarDealershipModel, default=-1, on_delete=models.CASCADE,
                                          related_name="profiles_staff")
    role = models.CharField(max_length=8, choices=StaffChoicesModel.choices)

    work_experience = models.IntegerField(default=0, blank=False)
    work_phone = models.CharField(blank=False, max_length=10)  # todo
    work_email = models.EmailField(blank=True)  # todo
