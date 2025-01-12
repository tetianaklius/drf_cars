from django.urls import path

from apps.cars.adverts.views import AdvertListCreateView

urlpatterns = [
    path("", AdvertListCreateView.as_view()),
]