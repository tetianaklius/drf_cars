from django.urls import path

from apps.cars.adverts.views import AdvertListView, AdvertAddPhotoView, AdvertRetrieveUpdateDestroyView, \
    AdvertListByUserIdView, AdvertDetailsView

urlpatterns = [
    path("", AdvertListView.as_view()),  # frontend done
    path("/<int:pk>", AdvertRetrieveUpdateDestroyView.as_view()),
    path("/<int:pk>/photo", AdvertAddPhotoView.as_view()),
    path("/my_adverts", AdvertListByUserIdView.as_view()),
    path("/details/<int:pk>", AdvertDetailsView.as_view()),  # frontend done
]