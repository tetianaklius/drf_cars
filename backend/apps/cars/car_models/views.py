from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView

from apps.cars.brands.models import BrandModel
from apps.cars.car_models.models import CarModelModel
from apps.cars.car_models.serializers import CarModelModelSerializer


class CarModelListCreateView(ListCreateAPIView):
    queryset = CarModelModel.objects.all()
    serializer_class = CarModelModelSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        brand_id = kwargs["pk"]
        brand = BrandModel.objects.get(id=brand_id)
        data = self.request.data
        serializer = CarModelModelSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(brand=brand)

        return Response(serializer.validated_data, status.HTTP_201_CREATED)

