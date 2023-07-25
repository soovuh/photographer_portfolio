from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n'))
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls', namespace='portfolio')),
    path('', include('home.urls', namespace='home')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('services/', include('services.urls', namespace='services')),
    path('reviews/', include('reviews.urls', namespace='reviews')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
