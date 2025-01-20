from django.urls import path

from apps.cars.car_dealership.views import CarDealershipListCreateView, CarDealershipAddAdvertView

urlpatterns = [
    path("", CarDealershipListCreateView.as_view()),
    path("/<int:pk>/adverts", CarDealershipAddAdvertView.as_view()),
]
