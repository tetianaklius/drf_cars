from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny

from apps.auth_user.user.serializers import UserModelSerializer
from core.services.jwt_service import JWTService, ActivateToken


class ActivateUserView(GenericAPIView):
    permission_classes = [AllowAny]

    def patch(self, *args, **kwargs):
        token = kwargs["token"]
        user = JWTService.verify_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserModelSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

