from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Listing
from .forms import ListingModelForm, ListingEditModelForm
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from .choices import price_choices, bedroom_choices
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from shortlist.models import Shortlist
# Create your views here.

#Return single listing
def listing(request, listing_id):
    #To retreive shortlisted property
    shortlisted = Shortlist.objects.raw('SELECT * FROM shortlist_shortlist WHERE listing_id = %d' % listing_id)
    listing = Listing.objects.raw('SELECT * FROM listings_listing WHERE id = %d' % listing_id)
    print(shortlisted)
    context = {
        'listing': listing,
        'shortlisted': shortlisted
    }
    return render(request, 'listings/listing.html', context)

# To search properties
@csrf_exempt
def search(request):
    queryset_list = Listing.objects.order_by('-price')
    if 'city' in request.GET:
        city = request.GET['city']
        print(city)
        if city:
            queryset_list = queryset_list.filter(city__icontains=city)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__icontains=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__icontains=price)

    if 'price' in request.GET and 'bedrooms' in request.GET:
        price = request.GET['price']
        bedrooms = request.GET['bedrooms']
        queryset_list = queryset_list.filter(price__icontains=price)&queryset_list.filter(bedrooms__icontains=bedrooms)

    if 'city' in request.GET and 'price' in request.GET:
        city = request.GET['city']
        price = request.GET['price']
        queryset_list = queryset_list.filter(city__icontains=city)&queryset_list.filter(price__icontains=price)
    
    if 'city' in request.GET and 'bedrooms' in request.GET:
        city = request.GET['city']
        bedrooms = request.GET['bedrooms']
        queryset_list = queryset_list.filter(city__icontains=city)&queryset_list.filter(bedrooms__icontains=bedrooms)

    paginator = Paginator(queryset_list, 4)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
      'listings':  paged_listings,
      'bedroom_choices': bedroom_choices,
      'price_choices': price_choices,
       'values': request.GET
    }
    return render(request, 'listings/search.html', context)

#To add property
@login_required(login_url='login')
def addlisting(request):
    user = request.user
    form = ListingModelForm()
    if request.method == 'POST':
        form = ListingModelForm(request.POST, request.FILES)
        if form.is_valid():
            action_type = request.POST['action_type']
            title = request.POST['title']
            property_type = request.POST['property_type']
            photo_main = request.FILES['photo_main']
            city = request.POST['city']
            address = request.POST['address']
            location = request.POST['location']
            price = request.POST['price']
            bedrooms = request.POST['bedrooms']
            bathrooms = request.POST['bathrooms']
            built_up_area = request.POST['built_up_area']
            carpet_area = request.POST['carpet_area']
            unit = request.POST['unit']
            transaction_type = request.POST['transaction_type']
            property_floor = request.POST['property_floor']
            ownership = request.POST['ownership']
            total_floors = request.POST['total_floors']
            availability = request.POST['availability']
            description = request.POST['description']
            listing = Listing(action_type=action_type, title=title, user=user, property_type=property_type, photo_main=photo_main, city=city, address=address, location=location, price=price, bedrooms=bedrooms, bathrooms=bathrooms, built_up_area=built_up_area, unit=unit, transaction_type=transaction_type, property_floor=property_floor, ownership=ownership, total_floors=total_floors, availability=availability, description=description, carpet_area=carpet_area)
            print(listing)
            listing.save()
            return JsonResponse({'error': False, 'message': 'Property added Successfully'})
        else:        
            return JsonResponse({'error': True, 'errors': form.errors})
        
        # return redirect('dashboard')
    return render(request, "listings/addlisting.html", {"form": form})

# To edit property
@login_required(login_url='login')
def editlisting(request, pk):
    listing = Listing.objects.get(id=int(pk))
    print(listing)
    form = ListingEditModelForm(instance=listing)
    if request.method == 'POST':
        form = ListingEditModelForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form':form}
    return render(request, "listings/editlisting.html", context)

# To Delete a property
@login_required(login_url='login')    
def deletelisting(request, pk):
    listing = Listing.objects.get(id=int(pk))
    print(listing)
    if request.method == "POST":
        listing.delete()
        return redirect('dashboard')
    context = {'item':listing}
    return render(request, 'listings/delete.html', context)

# Mark the location of a single listing on a map
def mapshow(request, pk):
    listing = Listing.objects.raw('SELECT * FROM listings_listing WHERE id = %d' % int(pk))
    print(listing)
    return render(request, 'listings/map.html', {'listing': listing})
    
