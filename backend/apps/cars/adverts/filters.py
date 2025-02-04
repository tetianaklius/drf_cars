from django_filters import rest_framework as filters


class AdvertFilter(filters.FilterSet):
    year_from = filters.NumberFilter(field_name="year", lookup_expr="gte")
    year_to = filters.NumberFilter(field_name="year", lookup_expr="lte")
    region_in = filters.BaseInFilter(field_name="region")
    city_in = filters.BaseInFilter(field_name="city")
    lt = filters.NumberFilter(field_name="price", lookup_expr="lt")
    # range = filters.RangeFilter(field_name="per_page")  # range_min=2&range_max=20
    order = filters.OrderingFilter(
        fields=(
            "id",
            "price",
            "mileage",
            "updated_at"
        )
    )  # order=name asc (# order=-name desc)
