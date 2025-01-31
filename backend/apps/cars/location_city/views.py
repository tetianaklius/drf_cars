from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView

from apps.cars.location_city.models import CityModel
from apps.cars.location_city.serializer import CityModelSerializer


class CityModelListCreateView(ListCreateAPIView):
    queryset = CityModel.objects.all()
    serializer_class = CityModelSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CityModelSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status.HTTP_201_CREATED)
