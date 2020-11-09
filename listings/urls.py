from django.urls import path

from . import views

urlpatterns = [
    path('<int:listing_id>/', views.listing, name='listing'),
    path('addlisting/', views.addlisting, name='addlisting'),
    path('search/', views.search, name='search'),
]