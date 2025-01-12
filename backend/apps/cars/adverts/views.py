from rest_framework.generics import ListCreateAPIView

from apps.cars.adverts.models import CarAdvertModel
from apps.cars.adverts.serializers import AdvertSerializer


class AdvertListCreateView(ListCreateAPIView):
    serializer_class = AdvertSerializer
    queryset = CarAdvertModel.objects.all()

