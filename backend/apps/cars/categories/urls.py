from django.urls import path

from .views import CarCategoryArrayListCreateView

urlpatterns = [
    path("/array", CarCategoryArrayListCreateView.as_view()),
]
