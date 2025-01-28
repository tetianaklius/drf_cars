from django.urls import path

from .views import CarModelListCreateView

urlpatterns = [
    path("/<int:pk>", CarModelListCreateView.as_view()),
]
