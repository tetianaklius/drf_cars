from django.urls import path

from apps.cars.location_city.views import CityModelListCreateView, CityModelArrayListCreateView

urlpatterns = [
    path("", CityModelListCreateView.as_view()),
    path("/array", CityModelArrayListCreateView.as_view()),
]
