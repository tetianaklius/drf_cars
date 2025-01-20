from rest_framework.generics import RetrieveUpdateDestroyAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from apps.auth_user.user.permissions import IsSuperUser
from apps.cars.adverts.filter import AdvertFilter
from apps.cars.adverts.models import CarAdvertModel
from apps.cars.adverts.serializers import AdvertSerializer, AdvertPhotoSerializer


class AdvertListView(ListAPIView):
    serializer_class = AdvertSerializer
    queryset = CarAdvertModel.objects.all()
    filterset_class = AdvertFilter
    permission_classes = (AllowAny,)


class AdvertRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdvertSerializer
    queryset = CarAdvertModel.objects.all()
    http_method_names = ["put", "patch", "delete"]
    permission_classes = [IsSuperUser,]


class AdvertAddPhotoView(UpdateAPIView):
    serializer_class = AdvertPhotoSerializer
    queryset = CarAdvertModel.objects.all()
    http_method_names = ["put"]

    def perform_update(self, serializer):
        advert = self.get_object()
        advert.photo.delete()
        super().perform_update(serializer)

