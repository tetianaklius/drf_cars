from django.conf.urls.static import static
from django.urls import include, path

from configs import settings

urlpatterns = [
    path("api/auth", include("apps.auth_user.auth.urls")),
    # path("", include("apps.cars.adverts.urls")),
    path("api/adverts", include("apps.cars.adverts.urls")),
    path("api/users", include("apps.auth_user.user.urls")),
    path("api/dealerships", include("apps.cars.car_dealership.urls")),
    path("api/car_models", include("apps.cars.car_model.urls")),
    path("api/brands", include("apps.cars.brand.urls")),
    path("api/cities", include("apps.cars.location_city.urls")),
    path("api/categories", include("apps.cars.categories.urls")),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
