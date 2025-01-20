from django.urls import path

from apps.cars.adverts.views import AdvertListView, AdvertAddPhotoView, AdvertRetrieveUpdateDestroyView

urlpatterns = [
    path("", AdvertListView.as_view()),
    path("/<int:pk>", AdvertRetrieveUpdateDestroyView.as_view()),
    path("/<int:pk>/photo", AdvertAddPhotoView.as_view()),
]