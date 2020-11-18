from django.urls import path

from . import views

urlpatterns = [
    path('<int:listing_id>/', views.listing, name='listing'),
    path('addlisting/', views.addlisting, name='addlisting'),
    path('search/', views.search, name='search'),
    path('editlisting/<str:pk>', views.editListing, name='editlisting'),
    path('deletelisting/<str:pk>', views.deleteListing, name='deletelisting'),
    path('mapshow/<str:pk>', views.mapshow, name='mapshow'),
]