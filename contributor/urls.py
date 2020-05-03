from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login, name='login'),
    path('c_signup', views.c_signup, name='c_signup'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('upload', views.upload, name='upload'),
    path('addContent', views.addContent, name='addContent'),
]