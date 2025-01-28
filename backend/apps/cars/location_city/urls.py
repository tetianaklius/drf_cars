from django.urls import path

from apps.cars.location_city.views import CityModelListCreateView

urlpatterns = [
    path("", CityModelListCreateView.as_view()),
]
