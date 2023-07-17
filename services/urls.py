from django.urls import path

from services import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
]
