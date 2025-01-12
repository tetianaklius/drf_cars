from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from apps.auth_user.user.managers import UserManager
from core.models import BaseModel


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = "auth_user"
        ordering = ["-id"]

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    objects = UserManager()


class ProfileModel(BaseModel):
    class Meta:
        db_table = "profile"
        # ordering = ["-id"]

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name="profile")
    objects = models.Manager()
