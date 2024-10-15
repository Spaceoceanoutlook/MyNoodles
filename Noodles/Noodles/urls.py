from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main_app.views import (
    noodle_list_view,
    country_noodle_list_view,
    manufacturer_noodle_list_view,
    recommendation_noodle_list_view,
    search,
    noodle,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("main_app.urls")),
    path("", noodle_list_view, name="noodle_list_view"),
    path(
        "noodles/country/<int:country_id>/",
        country_noodle_list_view,
        name="country_noodle_list_view",
    ),
    path(
        "noodles/manufacturer/<int:manufacturer_id>/",
        manufacturer_noodle_list_view,
        name="manufacturer_noodle_list_view",
    ),
    path(
        "recommendation/",
        recommendation_noodle_list_view,
        name="recommendation_noodle_list_view",
    ),
    path("search/", search, name="search"),
    path("noodle/<int:noodle_id>/", noodle, name="noodle"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
