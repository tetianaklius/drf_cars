from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView

from apps.auth_user.user.permissions import IsSuperUser
from apps.cars.adverts.models import CarAdvertModel
from apps.cars.adverts.serializers import AdvertSerializer, AdvertPhotoSerializer


class AdvertListCreateView(ListCreateAPIView):
    serializer_class = AdvertSerializer
    queryset = CarAdvertModel.objects.all()


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

