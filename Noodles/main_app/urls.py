from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    NoodlesViewSet,
    country_noodle_list_view,
    manufacturer_noodle_list_view,
)

router = DefaultRouter()
router.register(r"noodles", NoodlesViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
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
]
