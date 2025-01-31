from apps.auth_user.user import permissions


class IsCarDealershipAdminPermission(permissions.BasePermission):
    message = "User is not the admin"

    def has_permission(self, request, view):
        return (request.user.is_authenticated and
                request.user.is_staff and
                request.user.profile_staff.role == "Admin")

    # def has_object_permission(self, request, view, obj):
    #     return (request.user.is_authenticated and
    #             request.user.is_staff and
    #             request.user.profile_staff.car_dealership_id == obj.id and
    #             request.user.profile_staff.role == "Admin")


class IsCarDealershipManagerPermission(permissions.BasePermission):
    message = "User is not the manager"

    def has_permission(self, request, view):
        return (request.user.is_authenticated and
                request.user.is_staff and
                request.user.profile_staff.role == "Manager")

