from django.conf.urls.static import static
from django.urls import include, path

from configs import settings

urlpatterns = [
    path("api/auth", include("apps.auth_user.auth.urls")),
    path("api/adverts", include("apps.cars.adverts.urls")),
    path("api/adverts", include("apps.currency.urls")),
    path("api/users", include("apps.auth_user.user.urls")),
    path("api/dealerships", include("apps.cars.car_dealerships.urls")),
    path("api/car_models", include("apps.cars.car_models.urls")),
    path("api/brands", include("apps.cars.brands.urls")),
    path("api/cities", include("apps.cars.location_city.urls")),
    path("api/categories", include("apps.cars.categories.urls")),
    path("api/categories", include("apps.cars.brands.urls")),
    path("api/currency", include("apps.currency.urls")),
    path("api/posts", include("apps.posts.urls")),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
