from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('new_post/', views.new_post, name='new_post'),
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),

    # path('profile/',views.profile,name='profile'),
    # path('edit/profile',views.profile_edit,name='profile_edit'),


    # path('registration_form/', views.signup, name='signup'),
    # path('upload/', views.upload, name='upload'),
    # path('upload/', views.upload, name='upload'),
    # path('update/<int:post_id>', views.update_post, name='update'),
    # path('delete/<int:post_id>', views.upload_post, name='delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
