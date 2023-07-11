from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('portfolio.urls')),
    path('about/', include('home.urls')),

    path('admin/', admin.site.urls),
]
