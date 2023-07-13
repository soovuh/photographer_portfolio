from django.urls import path

from portfolio import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.all_categories, name='portfolio'),
    path('<int:pk>/', views.category_photos, name='category'),
    path('photo/<int:pk>', views.photo, name='photo')
]
