from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
# Create your views here.
def index(request):
    listings = Listing.objects.raw('SELECT * FROM listings_listing')
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
      'listings':  paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request):
    return render(request, 'listings/listing.html')
def search(request):
    return render(request, 'listings/search.html')