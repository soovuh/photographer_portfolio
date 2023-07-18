from django.urls import path

from reviews import views

app_name = 'reviews'

urlpatterns = [
    path('', views.all_reviews, name='all_reviews'),
]
