from django.urls import path

from apps.cars.car_dealerships.views import CarDealershipListCreateView, CarDealershipAddAdvertView

urlpatterns = [
    path("", CarDealershipListCreateView.as_view(), name="dealership_list_create"),
    path("/<int:pk>/adverts", CarDealershipAddAdvertView.as_view()),
]
