from django.urls import path
from . import views

urlpatterns = [
    path('shortlist', views.shortlist, name='shortlist')
]