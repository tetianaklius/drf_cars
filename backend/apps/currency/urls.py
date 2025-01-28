from django.urls import path

from .views import CurrencyPointCreateView, CurrencyPointUpdateView

urlpatterns = [
    path("/currency_point_add", CurrencyPointCreateView.as_view()),
    path("/currency_point_add/<str:name>", CurrencyPointUpdateView.as_view())
]