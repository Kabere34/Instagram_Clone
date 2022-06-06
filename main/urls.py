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
    path('profile/',views.profile,name='profile'),
    path('edit_profile',views.profile_edit,name='profile_edit'),
    path('comment/<int:post_id>',views.add_comment,name='comment'),
    path('search/', views.search_results,name='search_results'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
