from django.urls import path

from apps.cars.brands.views import BrandModelListCreateView

urlpatterns = [
    path("<int:pk>/brands", BrandModelListCreateView.as_view()),
]
