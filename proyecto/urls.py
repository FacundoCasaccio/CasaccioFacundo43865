from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from proyecto import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("aplication/", include("aplication.urls")),
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)