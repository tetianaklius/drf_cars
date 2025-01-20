from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from apps.cars.categories.models import CarCategoryModel
from apps.cars.categories.serializers import CarCategorySerializer


class CarCategoryArrayListCreateView(GenericAPIView):   # to add category array at one request
    queryset = CarCategoryModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        data = self.request.data
        arr = []
        for item in data:
            serializer = CarCategorySerializer(data=item)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            arr.append(serializer.data)

        return Response(arr, status.HTTP_201_CREATED)
