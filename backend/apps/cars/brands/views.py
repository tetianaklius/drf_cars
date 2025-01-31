from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView

from apps.cars.brands.models import BrandModel
from apps.cars.brands.serializers import BrandModelSerializer
from apps.cars.categories.models import CarCategoryModel


class BrandModelListCreateView(ListCreateAPIView):
    queryset = BrandModel.objects.all()
    serializer_class = BrandModelSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = BrandModelSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        category_id = kwargs["pk"]
        category = CarCategoryModel.objects.get(category_id=category_id)
        serializer.save(category=category)

        return Response(serializer.validated_data, status.HTTP_201_CREATED)
