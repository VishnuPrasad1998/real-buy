from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('', views.PropertyListing.as_view()),
    path('/featured', views.FeaturedListings.as_view()),
    path('/recent', views.RecentListings.as_view()),
    path('/search', views.PropertyListFilters.as_view()),
    path('/<int:pk>', views.ListingDetails.as_view()),  
]

urlpatterns = format_suffix_patterns(urlpatterns)