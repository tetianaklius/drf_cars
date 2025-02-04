from django_filters import rest_framework as filters


class UsersFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    age = filters.RangeFilter(field_name="age")  # age_min=27&age_max=28
    city = filters.CharFilter(field_name="city", lookup_expr="icontains")
    profession = filters.CharFilter(field_name="profession", lookup_expr="icontains")
    order = filters.OrderingFilter(
        fields=(
            "id",
            "age",
        )
    )
