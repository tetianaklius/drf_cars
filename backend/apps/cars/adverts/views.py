from rest_framework.generics import UpdateAPIView, ListAPIView, GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.sessions.models import Session


from apps.cars.adverts.filters import AdvertFilter
from apps.cars.adverts.models import CarAdvertModel
from apps.cars.adverts.serializers import AdvertSerializer, AdvertPhotoSerializer, AdvertListAllSerializer, \
    AdvertListByUserIdSerializer, AdvertUpdateSerializer, AdvertDetailsSerializer
from apps.visits_count.services import visit_add, get_visit_count
from core.checkers.profanity_checker import ProfanityChecker
from core.exceptions.profanity_check_exception import ProfanityCheckException
from core.pagination import CustomPagePagination
from core.services.avg_prices_service import get_avg_prices
# from core.services.sessions_service import register_session

# from django.contrib.user_sessions.models import Session


class AdvertListView(ListAPIView):             # all adverts list
    serializer_class = AdvertListAllSerializer
    queryset = CarAdvertModel.objects.filter(is_active=True)
    filterset_class = AdvertFilter
    pagination_class = CustomPagePagination
    permission_classes = (AllowAny,)

    # def get(self, request, *args, **kwargs):   ## todo here is start of sessions creating
    #     user = request.user
    #     session = request.session
    #     # session = Session.objects.get(session_key=request.session.session_key)
    #     # session = Session.objects.get(pk=user.id)
    #     register_session(user, request)
    #     print(session.keys())
    #     print("********************************")
    #
    # # >> > s.expire_date
    # # datetime.datetime(2005, 8, 20, 13, 35, 12)


class AdvertListByUserIdView(ListAPIView):           # adverts created by current user
    queryset = CarAdvertModel.objects.filter(is_visible=True)
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagePagination
    http_method_names = ["get"]

    def get(self, *args, **kwargs):
        adverts = self.queryset.filter(user_id=self.request.user.id)
        serializer = AdvertListByUserIdSerializer(adverts, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class AdvertRetrieveUpdateDestroyView(GenericAPIView):                  #update
    serializer_class = AdvertUpdateSerializer
    queryset = CarAdvertModel.objects.filter(is_visible=True)
    permission_classes = (IsAuthenticated,)
    http_method_names = ["patch", ]

    def patch(self, request, *args, **kwargs):
        advert = self.get_object()
        serializer = self.get_serializer(advert, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        res = ProfanityChecker.check_profanity(self, data=serializer.validated_data)
        if not res:
            if advert.profanity_edit_count > 4:
                serializer.save(is_active=False, is_visible=False)
                # надсилається лист менеджерові, щоб перевірив оголошення todo
                return Response(
                    {
                        "Message": "Because your advert contains profanity words, it has been sent to the manager "
                                   "for review. Expect a response within 24 hours",
                    },
                    status.HTTP_202_ACCEPTED)
            else:
                advert.profanity_edit_count += 1
                serializer.save(is_active=False)
                raise ProfanityCheckException
        else:
            serializer.save(profanity_edit_count=0, is_active=True)


class AdvertAddPhotoView(UpdateAPIView):
    serializer_class = AdvertPhotoSerializer
    queryset = CarAdvertModel.objects.all()
    http_method_names = ["put"]

    def perform_update(self, serializer):
        advert = self.get_object()
        advert.photo.delete()
        super().perform_update(serializer)


class AdvertDetailsView(GenericAPIView):
    queryset = CarAdvertModel.objects.filter(is_active=True)
    http_method_names = ["get"]
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        advert = self.get_object()
        user = self.request.user

        visit_add(self.request, advert.id)
        advert.counter = get_visit_count(advert.id, user)
        advert.avg_prices = get_avg_prices(advert, user)

        advert.created_at = advert.created_at.strftime("%m/%d/%Y, %H:%M:%S")
        advert.updated_at = advert.updated_at.strftime("%m/%d/%Y, %H:%M:%S")

        serializer = AdvertDetailsSerializer(advert)
        return Response(serializer.data, status.HTTP_200_OK)


class AdvertGetAllView(ListAPIView):
    queryset = CarAdvertModel.objects.filter(is_active=True, is_visible=True)
    serializer_class = AdvertDetailsSerializer
    pagination_class = CustomPagePagination
    filterset_class = AdvertFilter
    permission_classes = (AllowAny,)

