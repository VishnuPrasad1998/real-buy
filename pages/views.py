from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
# Create your views here.
def index(request):
    recent_listings = Listing.objects.raw('SELECT * FROM listings_listing ORDER BY posting_date DESC')
    context = {
        'recent_listings': recent_listings
    }
    return render(request, 'pages/index.html', context)