from django.urls import re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Documentation
schema_view = get_schema_view(
    openapi.Info(
        title="EXPRESS News API by TIMSON",
        default_version="v1",
        description="A rest api server for the express news\
 website written in Django, djangorestframework and make use of hackernews",
        terms_of_service="https://www.linkedin.com/in/timsonf",
        contact=openapi.Contact(email="mod.timson@gmail.com"),
        license=openapi.License(name="Timson Software License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
