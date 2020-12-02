from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Shortlist
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .resources import ShortlistResource

# To shortlist a property
@login_required(login_url='login')
def shortlist(request):
    if request.method == 'POST':
       listing_id = request.POST['listing_id']
       listing = request.POST['listing']
       name = request.POST['name']
       slot = request.POST['slot']
       message = request.POST['message']
       user_id = request.POST['user_id']
       client_email = request.POST['client_email']
       client_phone = request.POST['client_phone']
       realtor_email = request.POST['realtor_email']
       
       if request.user.is_authenticated:
           user_id = request.user.id
           has_contacted = Shortlist.objects.all().filter(listing_id=listing_id, user_id=user_id)
           if has_contacted:
               messages.error(request, "You have already shortlisted this property...!!!")
               return redirect('/listings/'+listing_id)
           else:
                if(realtor_email==request.user.email):
                    messages.error(request, "You can't shortlist property added by you...!!!")
                    return redirect('/listings/'+listing_id)

       shortlist = Shortlist(listing=listing, listing_id=listing_id, name=name, slot=slot, message=message, user_id=user_id )

       shortlist.save()

       send_mail(
           'Property Listing Inquiry',
           'There is been an inquiry for ' + listing + ' by '+ name +' and would love to visit the property tomorrow ' + slot + '. You can contact him/her in '+ 'Email id: ' +client_email + ' or ' + 'Phone number: ' + client_phone,
           'mini@gmail.com',
            [realtor_email],
           fail_silently=False
       )
       messages.success(request, 'Successfully shortlisted, Realtor will contact you soon...')
       return redirect('/listings/'+listing_id)
       
# To export shortlisted data as csv
def export(request):
    shortlist_resource = ShortlistResource()
    dataset = shortlist_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="shortlisted.csv"'
    return response