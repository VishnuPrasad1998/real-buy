from django.urls import path
from .import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout/',views.logoutUser, name='logout'),
    path('register/',views.registerPage, name='register'),
    path('login/',views.loginPage, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('profileupdate/',views.profileupdate, name='profileupdate'),

    path('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
    name="reset_password"),

    path('reset_password_sent/',
    auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
    name="password_reset_done"),

    path('reset/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
    name="password_reset_confirm"),

    path('reset_password_complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
    name="password_reset_complete"),

]