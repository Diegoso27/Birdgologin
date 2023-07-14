from django.urls import path
from . import views


urlpatterns = [
  path('sign_up', views.register_user, name='register'),
  path('login', views.login_user, name='login_user'),
  path('logout', views.logout_user, name='logout_user'),
  path('', views.home, name='home')
]