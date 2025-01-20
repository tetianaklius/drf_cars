REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "apps.auth_user.user.permissions.IsSuperUser",
    ],
    "EXCEPTION_HANDLER": "core.handlers.error_handler.error_handler",
    "DEFAULT_PAGINATION_CLASS": "core.pagination.CustomPagePagination",
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
    ),
}
