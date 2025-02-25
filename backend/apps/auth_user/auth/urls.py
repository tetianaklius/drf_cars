from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.auth_user.auth.views import ActivateUserView, RecoveryRequestView, RecoveryPasswordView, SocketTokenView

urlpatterns = [
    path("", TokenObtainPairView.as_view(), name="auth_login"),
    path("/refresh", TokenRefreshView.as_view(), name="auth_refresh"),
    path("/activate/<str:token>", ActivateUserView.as_view(), name="auth_activate"),

    path('/recovery', RecoveryRequestView.as_view(), name="auth_recovery"),
    path('/recovery/<str:token>', RecoveryPasswordView.as_view(), name="auth_recovery_password"),
    path('/socket', SocketTokenView.as_view(), name="auth_socket"),
]
