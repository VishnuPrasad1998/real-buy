from django.urls import path
from . import views

urlpatterns = [
    path('', views.visualize, name='visualize'),
]