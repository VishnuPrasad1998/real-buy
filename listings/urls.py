from django.urls import path

from . import views

urlpatterns = [
    path('recent/', views.recent, name='recent'),
    path('<int:listing_id>/', views.listing, name='listing'),
    path('featured/', views.featured, name='featured'),
]