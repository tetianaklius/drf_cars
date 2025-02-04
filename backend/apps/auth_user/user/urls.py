from django.urls import path

from apps.auth_user.user.views import SendEmailTestView, BlockUserView, UnBlockUserView, \
    UserToAdminView, UsersListView, UserCreateView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("", UsersListView.as_view(), name="users_list"),
    path("/create", UserCreateView.as_view(), name="user_create"),
    path("/<int:pk>", UserRetrieveUpdateDestroyAPIView.as_view(), name="user_by_id"),
    path("/test", SendEmailTestView.as_view(), name="send_email_test"),
    path('/<int:pk>/block', BlockUserView.as_view(), name="user_block"),
    path('/<int:pk>/unblock', UnBlockUserView.as_view(), name="user_unblock"),
    path('/<int:pk>/to_admin', UserToAdminView.as_view(), name="user_to_admin"),
]
