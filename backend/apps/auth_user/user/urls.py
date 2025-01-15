from django.urls import path

from apps.auth_user.user.views import UserListCreateView, SendEmailTestView

urlpatterns = [
    path("", UserListCreateView.as_view(), name="user_list_create"),
    path("/test", SendEmailTestView.as_view(), name="send_email_test"),
]