from django.db import models
from django.contrib.auth import get_user_model
from django.core import validators as v

from core.models import BaseModel

UserModel = get_user_model()


class PostLabelChoicesModel(models.TextChoices):
    TRAVELS = "Travels"
    FOOD = "Food"
    ROUTINE = "Routine"
    TECHNICS = "Technics"
    HEALTH = "Health"
    EDUCATION = "Education"
    STORY_OF_THE_DAY = "Story Of The Day"
    WORK = "Work"
    HOME = "Home"
    PRESENTS = "Presents"
    DECOR = "Decor"
    HANDMADE = "Handmade"
    SOCIAL = "Social"
    POLITICS = "Politics"
    ARTS = "Arts"
    LITERATURE = "Literature"
    MOVIES = "Movies"
    HOBBY = "Hobby"
    SELF_DEVELOPMENT = "Self Development"
    OTHER = "Other"


class PostModel(BaseModel):
    class Meta:
        db_table = "posts"

    is_active = models.BooleanField(default=True)
    is_visible = models.BooleanField(default=True)

    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=60, blank=False)
    text = models.TextField(max_length=2000, blank=False, null=False)
    label = models.CharField(max_length=16, choices=PostLabelChoicesModel.choices)
    # photo = models.ImageField(upload_to=upload_adv_photo, blank=True)
    profanity_edit_count = models.IntegerField(default=0, validators=[v.MinValueValidator(0)])
