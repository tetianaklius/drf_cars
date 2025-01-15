import os

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from apps.auth_user.user.models import UserModel
from apps.auth_user.user.serializers import UserModelSerializer


class UserListCreateView(ListCreateAPIView):
    model = UserModel
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [AllowAny]


class SendEmailTestView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        template = get_template("test_email.html")
        html_content = template.render({"name": "django"})
        msg = EmailMultiAlternatives(
            subject="Test email",
            from_email=os.environ.get("EMAIL_HOST_USER"),
            to=["tetyanaklyus@gmail.com"]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return Response({"message": "Email sent"}, status.HTTP_200_OK)
