from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from apps.cars.categories.models import CarCategoryModel
from apps.cars.categories.serializers import CategoryModelSerializer


class CarCategoryListCreateView(GenericAPIView):
    queryset = CarCategoryModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CategoryModelSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status.HTTP_201_CREATED)
