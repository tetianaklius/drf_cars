from django.urls import path

from .views import CarModelListCreateView, CarModelArrayListCreateView

urlpatterns = [
    path("", CarModelListCreateView.as_view()),
    path("/array", CarModelArrayListCreateView.as_view()),
]
