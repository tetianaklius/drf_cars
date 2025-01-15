from django.conf.urls.static import static
from django.urls import include, path

from configs import settings

urlpatterns = [
    path("api/auth", include("apps.auth_user.auth.urls")),
    # path("", include("apps.cars.adverts.urls")),
    path("api/adverts", include("apps.cars.adverts.urls")),
    path("api/users", include('apps.auth_user.user.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
