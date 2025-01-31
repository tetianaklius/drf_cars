from django.contrib.auth.models import Group
from guardian.ctypes import get_content_type
from guardian.models.models import UserObjectPermission

# admin_dealership = Group.objects.get(name="admin_dealership")

    # def assign_permissions(group):


# UserObjectPermission.objects.assign_perm(user_or_group=admin_dealership, perm="delete_cardealershipmodel")
# UserObjectPermission.objects .assign_perm(user_or_group=admin_dealership, perm="change_caradvertmodel")



