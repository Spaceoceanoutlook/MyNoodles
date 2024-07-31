from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoodlesViewSet


router = DefaultRouter()
router.register(r"noodles", NoodlesViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
