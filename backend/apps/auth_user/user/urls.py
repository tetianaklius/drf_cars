from django.urls import path

from apps.auth_user.user.views import UserListCreateView, SendEmailTestView, BlockUserView, UnBlockUserView, \
    UserToAdminView

urlpatterns = [
    path("", UserListCreateView.as_view(), name="user_list_create"),
    path("/test", SendEmailTestView.as_view(), name="send_email_test"),

    path('/<int:pk>/block', BlockUserView.as_view(), name="user_block"),
    path('/<int:pk>/unblock', UnBlockUserView.as_view(), name="user_unblock"),
    path('/<int:pk>/to_admin', UserToAdminView.as_view(), name="user_to_admin"),
]
