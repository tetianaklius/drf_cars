from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView

from apps.cars.adverts.serializers import AdvertSerializer
from apps.cars.car_dealership.models import CarDealershipModel
from apps.cars.car_dealership.serializers import CarDealershipSerializer
from core.checkers.profanity_checker import ProfanityChecker
from core.exceptions.profanity_check_exception import ProfanityCheckException


class CarDealershipListCreateView(ListCreateAPIView):
    serializer_class = CarDealershipSerializer
    queryset = CarDealershipModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CarDealershipAddAdvertView(ListCreateAPIView):
    queryset = CarDealershipModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        car_dealership = self.get_object()
        serializer = AdvertSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        res = ProfanityChecker.check_profanity(self, data=serializer.validated_data)              #
        if res:
            serializer.save(car_dealership_id=car_dealership, is_active=True)
        else:
            raise ProfanityCheckException
        car_dealership_serializer = CarDealershipSerializer(car_dealership)
        return Response(car_dealership_serializer.data, status.HTTP_201_CREATED)

    # def perform_update(self, serializer):          # todo
    #     if serializer.count == 3:
    #         self.instance.is_active = False
    #         # надсилається лист менеджерові, щоб перевірив оголошення
    #         return
    #     serializer.count += 1
