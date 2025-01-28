from django.urls import path

from .views import CarCategoryListCreateView

urlpatterns = [
    path("", CarCategoryListCreateView.as_view()),
]
