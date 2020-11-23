from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('/register', views.RegisterUser.as_view()),
    path('/login', views.LoginUser.as_view()),
    path('/logout', views.Logout.as_view()),
    path('/profileupdate/<int:pk>', views.UpdateProfile.as_view()),  
]

urlpatterns = format_suffix_patterns(urlpatterns)