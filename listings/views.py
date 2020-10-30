from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from .choices import price_choices, bedroom_choices
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

def listing(request, listing_id):
    listing = Listing.objects.raw('SELECT * FROM listings_listing WHERE id = %d' % listing_id)
    return render(request, 'listings/listing.html', {'listing': listing})

def search(request):
    queryset_list = Listing.objects.order_by('-posting_date')
    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__icontains=city)

    # Bedroom
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

  # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    if 'price' in request.GET and 'bedrooms' in request.GET:
        price = request.GET['price']
        bedrooms = request.GET['bedrooms']
        queryset_list = queryset_list.filter(price__lte=price)&queryset_list.filter(bedrooms__lte=bedrooms)

    if 'city' in request.GET and 'price' in request.GET:
        city = request.GET['city']
        price = request.GET['price']
        queryset_list = queryset_list.filter(city__icontains=city)&queryset_list.filter(price__lte=price)
    
    if 'city' in request.GET and 'bedrooms' in request.GET:
        city = request.GET['city']
        bedrooms = request.GET['bedrooms']
        queryset_list = queryset_list.filter(city__icontains=city)&queryset_list.filter(bedrooms__lte=bedrooms)

    context = {
      'bedroom_choices': bedroom_choices,
      'price_choices': price_choices,
      'listings': queryset_list,
      'values': request.GET
    }
    return render(request, 'listings/search.html', context)