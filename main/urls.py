from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('update/<int:post_id>', views.update_post, name='upload'),
    path('delete/', views.upload_post, name='upload'),
]

