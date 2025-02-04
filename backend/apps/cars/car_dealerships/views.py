from django.db.transaction import atomic
from django.contrib.auth.models import Group, ContentType

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response
from guardian.models.models import GroupObjectPermission

from apps import profile_staff
from apps.cars import adverts
from apps.cars.adverts.serializers import AdvertSerializer
from apps.cars.car_dealerships.models import CarDealershipModel
from apps.cars.car_dealerships.serializers import CarDealershipSerializer
from apps.profile_staff.models import ProfileStaffModel, StaffChoicesModel
from core.checkers.profanity_checker import ProfanityChecker
from core.exceptions.profanity_check_exception import ProfanityCheckException
from core.pagination import CustomPagePagination
from core.permissions.staff_dealership_permissions import IsCarDealershipManagerPermission, \
    IsCarDealershipAdminPermission


class CarDealershipListCreateView(ListCreateAPIView):
    serializer_class = CarDealershipSerializer
    queryset = CarDealershipModel.objects.all()
    pagination_class = CustomPagePagination
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @atomic
    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = CarDealershipSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=user, is_active=False)
        car_dealership = CarDealershipModel.objects.get(id=serializer.data["id"])
        ProfileStaffModel.objects.create(user_id=user, role=StaffChoicesModel.ADMIN,
                                         car_dealership_id=car_dealership)
        # створюємо групу адмінів для цього автосалону
        admin_dealership = Group.objects.create(name=f"admin_dealership {car_dealership.id}")
        # додаємо адміна до групи адмінів
        user.groups.add(admin_dealership)
        # створюємо об'єкт у таблиці ґардіан із дозволами (1/4 або 2/4, 3/4, 4/4) для групи для конкретного автосалону
        content_type = ContentType.objects.get_for_model(car_dealership)
        GroupObjectPermission.objects.create(object_pk=car_dealership.id, content_type_id=content_type.id,
                                             permission_id=94, group_id=admin_dealership.id)
        GroupObjectPermission.objects.create(object_pk=car_dealership.id, content_type_id=content_type.id,
                                             permission_id=95, group_id=admin_dealership.id)
        GroupObjectPermission.objects.create(object_pk=car_dealership.id, content_type_id=content_type.id,
                                             permission_id=96, group_id=admin_dealership.id)
        content_type = ContentType.objects.get_for_model(adverts)
        GroupObjectPermission.objects.create(object_pk=car_dealership.id, content_type_id=content_type.id,
                                             permission_id=78, group_id=admin_dealership.id)
        GroupObjectPermission.objects.create(object_pk=car_dealership.id, content_type_id=content_type.id,
                                             permission_id=80, group_id=admin_dealership.id)

        # створюємо групи мереджерок, продавців, механіків для цього автосалону і надаємо дозволи для цих груп

        # managers
        manager_dealership = Group.objects.create(name=f"manager_dealership {car_dealership.id}")
        # for car_dealership
        content_type = ContentType.objects.get_for_model(car_dealership)
        GroupObjectPermission.objects.create(object_pk=car_dealership.id, content_type_id=content_type.id,
                                             permission_id=94, group_id=manager_dealership.id)
        GroupObjectPermission.objects.create(object_pk=car_dealership.id, content_type_id=content_type.id,
                                             permission_id=96, group_id=manager_dealership.id)
        # for adverts
        content_type = ContentType.objects.get_for_model(adverts)
        GroupObjectPermission.objects.create(object_pk=car_dealership.id, content_type_id=content_type.id,
                                             permission_id=78, group_id=manager_dealership.id)
        GroupObjectPermission.objects.create(object_pk=car_dealership.id, content_type_id=content_type.id,
                                             permission_id=80, group_id=manager_dealership.id)
        # for profile_staff
        content_type = ContentType.objects.get_for_model(profile_staff)
        GroupObjectPermission.objects.create(object_pk=car_dealership.id, content_type_id=content_type.id,
                                             permission_id=122, group_id=manager_dealership.id)
        GroupObjectPermission.objects.create(object_pk=car_dealership.id, content_type_id=content_type.id,
                                             permission_id=123, group_id=manager_dealership.id)
        GroupObjectPermission.objects.create(object_pk=car_dealership.id, content_type_id=content_type.id,
                                             permission_id=124, group_id=manager_dealership.id)
        # GroupObjectPermission.objects.assign_perm(user_or_group=user, perm="change_cardealershipmodel",
        #                                           obj=car_dealership)

        # sales
        sales_dealership = Group.objects.create(name=f"sales_dealership {car_dealership.id}")
        # for adverts
        content_type = ContentType.objects.get_for_model(adverts)
        GroupObjectPermission.objects.create(object_pk=car_dealership.id, content_type_id=content_type.id,
                                             permission_id=77, group_id=sales_dealership.id)
        GroupObjectPermission.objects.create(object_pk=car_dealership.id, content_type_id=content_type.id,
                                             permission_id=78, group_id=sales_dealership.id)
        GroupObjectPermission.objects.create(object_pk=car_dealership.id, content_type_id=content_type.id,
                                             permission_id=79, group_id=sales_dealership.id)
        GroupObjectPermission.objects.create(object_pk=car_dealership.id, content_type_id=content_type.id,
                                             permission_id=80, group_id=sales_dealership.id)

        # mechanics
        mechanic_dealership = Group.objects.create(name=f"mechanic_dealership {car_dealership.id}")
        # for car_dealership
        content_type = ContentType.objects.get_for_model(car_dealership)
        GroupObjectPermission.objects.create(object_pk=car_dealership.id, content_type_id=content_type.id,
                                             permission_id=96, group_id=mechanic_dealership.id)
        # for adverts
        content_type = ContentType.objects.get_for_model(adverts)
        GroupObjectPermission.objects.create(object_pk=car_dealership.id, content_type_id=content_type.id,
                                             permission_id=80, group_id=mechanic_dealership.id)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CarDealershipRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    # serializer_class = CarDealershipSerializer
    queryset = CarDealershipModel.objects.all()
    permission_classes = (AllowAny,)  # todo

    # def get(self, request, *args, **kwargs):
    #     # serializer_class = CarDealershipSerializer # for all
    #     user = request.user
    #     dealership = self.get_object()
    #     # if not user.has_perm("car_dealerships.view_cardealershipmodel"):
    #     #     return Response(data={"Sorry, you don`t have permission to this action."}, status=status.HTTP_403_FORBIDDEN)
    #
    #     print(get_perms(user, dealership))
    #     print(user.groups.all())
    #
    #     # if user.has_perm(94, 18):
    #     #     # if dealership.id == user.profile_staff.car_dealership_id.id:
    #
    #     serializer = self.get_serializer(dealership)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        # serializer for update
        # permission поставити
        user = request.user
        car_dealership = self.get_object()
        if (
                (IsCarDealershipManagerPermission() or IsCarDealershipAdminPermission())
                and
                (f"admin_dealership {car_dealership.id}" in user.groups.all() or
                 f"manager_dealership {car_dealership.id}" in user.groups.all())
        ):
            serializer = CarDealershipSerializer(car_dealership, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("You don`t have permission to edit car dealership information",
                            status=status.HTTP_200_OK)


        # detroy тільки адмін


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
