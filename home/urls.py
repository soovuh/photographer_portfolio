from django.urls import path

from home import views

app_name = 'home'

urlpatterns = [
    path('about/', views.index, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]
