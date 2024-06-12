from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("movieDatabase/", include("movieDatabase.urls")),
    path("admin/", admin.site.urls),
]
