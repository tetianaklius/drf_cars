from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from apps.auth_user.user.managers import UserManager
from core.models import BaseModel


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = "auth_user"
        ordering = ["-id"]

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    objects = UserManager()


class ProfileModel(BaseModel):
    class Meta:
        db_table = "profile"
        ordering = ["-id"]

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    premium_acc = models.BooleanField(default=False)

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name="profile")
    # objects = models.Manager()


# class ProfileModel(BaseModel):
#     class Meta:
#         db_table = "profile"
#         ordering = ["-id"]
#
#     user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name="profile")
#
#     name = models.CharField(max_length=20)
#     surname = models.CharField(max_length=20)
#     age = models.IntegerField(max_length=130)
#     phone = models.CharField(max_length=20, unique=True, blank=True)
#     city = models.CharField(max_length=30)
#     profession = models.CharField(max_length=40, blank=True)
#     interests = models.CharField(max_length=150, blank=True)
#
#     # objects = models.Manager()
