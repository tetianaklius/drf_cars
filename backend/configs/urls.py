from django.urls import include, path

urlpatterns = [
    path("auth", include("apps.auth_user.auth.urls")),
    path("", include("apps.cars.adverts.urls")),
    path("adverts", include("apps.cars.adverts.urls")),
    # path('users', include('apps.user.urls')),

]