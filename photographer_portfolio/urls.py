from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('portfolio.urls')),
    path('about/', include('home.urls')),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)

