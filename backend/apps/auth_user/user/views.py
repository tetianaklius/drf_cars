import os

from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.auth_user.user.filters import UsersFilter
from apps.auth_user.user.models import ProfileModel
from apps.auth_user.user.serializers import UserModelSerializer
from core.pagination import CustomPagePagination

UserModel = get_user_model()


class UsersListView(ListAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = UserModelSerializer
    pagination_class = CustomPagePagination
    permission_classes = (IsAuthenticated,)
    filterset_class = UsersFilter


class UserCreateView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = (AllowAny,)


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        if self.kwargs["pk"]:
            searched_id = self.kwargs["pk"]
            user = UserModel.objects.filter(id=searched_id).first()
            if user:
                return Response(self.get_serializer(user).data, status=status.HTTP_200_OK)
            else:
                return Response("User not found", status=status.HTTP_404_NOT_FOUND)
        if self.kwargs["email"]:
            searched_email = self.kwargs["email"]
            user = UserModel.objects.filter(email=searched_email).first()
            if user:
                return Response(self.get_serializer(user).data, status=status.HTTP_200_OK)
            else:
                return Response("User not found", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("To search user you should write user id or user email.",
                            status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        user = self.request.user
        user_to_update = self.get_object()
        if user.is_authenticated and user.id == user_to_update.id:
            serializer = self.get_serializer(user_to_update, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    "Message": "You can edit only your personal account.",
                },
                status.HTTP_403_FORBIDDEN
            )

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        user_to_delete = self.get_object()
        if user.is_authenticated and user.id == user_to_delete.id:
            user_to_delete.destroy()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {
                "Message": "You can delete only your personal account.",
            },
            status.HTTP_403_FORBIDDEN
        )


class BlockUserView(GenericAPIView):
    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
            user.save()

        serializer = UserModelSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UnBlockUserView(GenericAPIView):

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = True
            user.save()

        serializer = UserModelSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserToAdminView(GenericAPIView):

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()

        serializer = UserModelSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
