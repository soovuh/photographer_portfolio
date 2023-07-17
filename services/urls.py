from django.urls import path

from services import views

app_name = 'services'

urlpatterns = [
    path('', views.all_services, name='all_services'),
]
