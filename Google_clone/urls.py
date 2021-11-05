from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home_images', views.home_images, name='home_images'),
    path('base', views.base, name='base'),
    path('base_images', views.base_images, name='base_images'),
    path('searches/<search>/', views.searches, name='searches'),
    path('images/<search>', views.images, name='images'),
    path('videos/<search>', views.videos, name='videos'),
    path('news/<search>', views.news, name='news'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('manage_account', views.account, name='manage_account'),
    path('profile', views.profile, name='profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('change_password',
         views.change_passwrd, name='change_passwrd'),
    path('password_reset', views.reset_passwrd, name='password_reset'),
    # path('reset_password_done', views.reset_passwrd_done, name='reset_passwrd')
    # path('logout', views.logout, name='log_out'),
]
