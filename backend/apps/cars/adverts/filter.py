from django_filters import rest_framework as filters


class AdvertFilter(filters.FilterSet):
    lt = filters.NumberFilter(field_name="price", lookup_expr="lt")
    range = filters.RangeFilter(field_name="per_page")  # range_min=2&range_max=20
    price_in = filters.BaseInFilter(field_name="price")  # price_in=30,35,25
    order = filters.OrderingFilter(
        fields=(
            "id",
            "price",
        )
    )  # order=name asc (# order=-name desc)
