from django.urls import path
from . import views

urlpatterns = [
    path('', views.Visualize, name='visualize'),
]