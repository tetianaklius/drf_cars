# from django.db import models
# from django.contrib.sessions.models import Session
# from django.contrib.auth import get_user_model
#
# UserModel = get_user_model()
#
#
# class UserSession(models.Model):     ## todo here is start of sessions creating
#     user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
#     session = models.OneToOneField(Session, on_delete=models.CASCADE)
#
#     session_start = models.DateTimeField(auto_now_add=True)
