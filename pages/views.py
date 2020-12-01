from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from listings.choices import price_choices, bedroom_choices
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from shortlist.models import Shortlist
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    user = request.user
    shortlisted = Shortlist.objects.filter(user_id=user.id).values_list('listing_id', flat=True)
    
    featured_listings = Listing.objects.raw('SELECT * FROM listings_listing ORDER BY price DESC')
    recent_listings = Listing.objects.raw('SELECT * FROM listings_listing ORDER BY posting_date DESC LIMIT 9')
    paginator = Paginator(featured_listings, 5)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'recent_listings': recent_listings,
        'featured_listings': paged_listings,
        'shortlisted': shortlisted
    }
    return render(request, 'pages/index.html', context)

def searchdetails(request):
    queryset_list = Listing.objects.order_by('-price').filter(action_type="ONSALE")
    paginator = Paginator(queryset_list, 4)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    if request.method == 'POST':
       keywords = request.POST['keywords']
       status = request.POST['options']
       print(status)
       if keywords:
            queryset_list = (queryset_list.filter(city__icontains=keywords)|queryset_list.filter(title__icontains=keywords)|queryset_list.filter(description__icontains=keywords)|queryset_list.filter(location__icontains=keywords))&(queryset_list.filter(action_type__icontains=status)|queryset_list.filter(availability__icontains=status))
            paginator = Paginator(queryset_list, 4)
            page = request.GET.get('page')
            paged_listings = paginator.get_page(page)
            
    context = {
        'listings': paged_listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(request, 'listings/search.html', context)