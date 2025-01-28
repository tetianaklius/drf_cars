from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView

from apps.cars.adverts.serializers import AdvertSerializer
from apps.cars.car_dealerships.models import CarDealershipModel
from apps.cars.car_dealerships.serializers import CarDealershipSerializer
from core.checkers.profanity_checker import ProfanityChecker
from core.exceptions.profanity_check_exception import ProfanityCheckException


class CarDealershipListCreateView(ListCreateAPIView):
    serializer_class = CarDealershipSerializer
    queryset = CarDealershipModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CarDealershipAddAdvertView(GenericAPIView):
    queryset = CarDealershipModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        car_dealership = self.get_object()
        user = self.request.user
        data = self.request.data
        adverts_count = self.queryset.filter(user_id=self.request.user.id).count()

        if not user.profile.premium_acc and adverts_count:
            return Response(f"account is premium = {user.profile.premium_acc},"
                            f" adverts_count = {adverts_count}",
                            status.HTTP_403_FORBIDDEN)

        serializer = AdvertSerializer(data=data, context={"price_init": data["price"]})
        serializer.is_valid(raise_exception=True)

        res = ProfanityChecker.check_profanity(self, data=serializer.validated_data)
        if res:
            serializer.save(car_dealership_id=car_dealership, profanity_edit_count=0, is_active=True, user_id=user)
        else:
            serializer.save(car_dealership_id=car_dealership, is_active=False, profanity_edit_count=1, user_id=user)
            raise ProfanityCheckException
        car_dealership_serializer = CarDealershipSerializer(car_dealership)
        return Response(car_dealership_serializer.data, status.HTTP_201_CREATED)
