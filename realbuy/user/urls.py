from django.urls import path
from .import views
from django.conf.urls import url


urlpatterns = [
    path('',views.home, name='home'),
    path('logout/',views.logoutUser, name='logout'),
    path('register/',views.registerPage, name='register'),
    path('login/',views.loginPage, name='login'),
]