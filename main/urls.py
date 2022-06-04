from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('create_post/', views.create_post, name='create_post'),
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    
    # path('registration_form/', views.signup, name='signup'),
    # path('upload/', views.upload, name='upload'),
    # path('upload/', views.upload, name='upload'),
    # path('update/<int:post_id>', views.update_post, name='update'),
    # path('delete/<int:post_id>', views.upload_post, name='delete'),
]

