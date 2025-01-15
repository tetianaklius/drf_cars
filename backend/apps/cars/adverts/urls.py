from django.urls import path

from apps.cars.adverts.views import AdvertListCreateView, AdvertAddPhotoView, AdvertRetrieveUpdateDestroyView

urlpatterns = [
    path("", AdvertListCreateView.as_view()),
    path("/<int:pk>", AdvertRetrieveUpdateDestroyView.as_view()),
    path("/<int:pk>/photo", AdvertAddPhotoView.as_view()),
]