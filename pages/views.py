from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
# Create your views here.
def index(request):
    featured_listings = Listing.objects.raw('SELECT * FROM listings_listing ORDER BY price DESC')
    recent_listings = Listing.objects.raw('SELECT * FROM listings_listing ORDER BY posting_date DESC LIMIT 9')
    paginator = Paginator(featured_listings, 5)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'recent_listings': recent_listings,
        'featured_listings': paged_listings
    }
    return render(request, 'pages/index.html', context)
