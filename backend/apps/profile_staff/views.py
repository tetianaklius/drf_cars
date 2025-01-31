from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from apps.cars.car_dealerships.models import CarDealershipModel
from apps.profile_staff.models import ProfileStaffModel
from apps.profile_staff.serializer import ProfileStaffModelSerializer
from core.permissions.staff_dealership_permissions import IsCarDealershipManagerPermission, \
    IsCarDealershipAdminPermission

UserModel = get_user_model()


class UserToDealershipStaffUpdateView(RetrieveUpdateAPIView):  # todo
    serializer_class = ProfileStaffModelSerializer
    queryset = ProfileStaffModel.objects.all()
    permission_classes = (IsCarDealershipManagerPermission, IsCarDealershipAdminPermission)

    # на тому моменті, коли profile_staff стає is_active=True (менеджер/адмін автосалону це робить),
    # працівники додаються до груп;

    def update(self, request, *args, **kwargs):
        # method for #1 admins and #2 managers
        user = self.request.user
        # try:
        car_dealership = CarDealershipModel.objects.get(id=user.profile_staff.dealership_id.id)

        # 1 # if request.user is admin
        group_name = f"admin_dealership {car_dealership.id}"
        group = Group.objects.get(name=group_name)
        if group in user.groups.all():
            user_to_update = UserModel.objects.get(id=kwargs["user_id"])
            serializer = ProfileStaffModelSerializer(request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(is_active=True)
            # try:
            if serializer.data.role == "Admin":
                group = Group.objects.get(name=f"admin_dealership {car_dealership.id}")
                user_to_update.groups.add(group)
            elif serializer.data.role == "Manager":
                group = Group.objects.get(name=f"manager_dealership {car_dealership.id}")
                user_to_update.groups.add(group)
            else:
                return Response({
                    "Details": "Sorry, contact your manager(s) to do this update"}, status=status.HTTP_403_FORBIDDEN
                )

            return Response(
                {
                    "Message": "User is updated successfully",
                    "User staff profile": serializer.data,
                    "User groups": [f"\n{group.name}\n" for group in user.groups.all()]
                }, status=status.HTTP_200_OK
            )

        # 2 # if request.user is manager
        group_name = f"manager_dealership {car_dealership.id}"
        group = Group.objects.get(name=group_name)
        if group in user.groups.all():
            user_to_update = UserModel.objects.get(id=kwargs["user_id"])
            serializer = ProfileStaffModelSerializer(request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(is_active=True)
            # try:
            if serializer.data.role == "Sales":
                group = Group.objects.get(name=f"sales_dealership {request.user.profile_staff.car_dealership_id.id}")
                user_to_update.groups.add(group)
            elif serializer.data.role == "Mechanic":
                group = Group.objects.get(name=f"mechanic_dealership {request.user.profile_staff.car_dealership_id.id}")
                user_to_update.groups.add(group)
            else:
                return Response({
                    "Details": "You don`t have permission to do this update"}, status=status.HTTP_403_FORBIDDEN
                )

            return Response(
                {
                    "Message": "User is updated successfully",
                    "User staff profile": serializer.data,
                    "User groups": [f"\n{group.name}\n" for group in user.groups.all()]
                }, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "Details": "You are neither admin no manager of this car dealership. "
                               "You don`t have permission to this action"}, status=status.HTTP_403_FORBIDDEN
            )
