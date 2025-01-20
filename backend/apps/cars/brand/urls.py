from django.urls import path

from apps.cars.brand.views import BrandModelListCreateView, BrandModelArrayListCreateView

urlpatterns = [
    path("", BrandModelListCreateView.as_view()),
    path("/array", BrandModelArrayListCreateView.as_view()),
]
