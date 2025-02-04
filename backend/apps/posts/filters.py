import datetime

from django_filters import rest_framework as filters

from apps.posts.models import PostLabelChoicesModel


class PostsFilter(filters.FilterSet):
    label = filters.ChoiceFilter("label", choices=PostLabelChoicesModel.choices)
    date_from = filters.DateTimeFilter(field_name="created_at", lookup_expr="gte")
    # date_from = filters.DateTimeFilter(field_name="created_at", created_at__date__gt=datetime.date(...))
    order = filters.OrderingFilter(
        fields=(
            "id",
            "updated_at"
        )
    )
