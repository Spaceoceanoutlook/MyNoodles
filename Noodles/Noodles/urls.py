from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main_app.views import noodle_list_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("main_app.urls")),
    path("noodles/", noodle_list_view, name="noodle_list_view"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
