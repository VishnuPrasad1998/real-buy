from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from contactus.models import Contactus
from .forms import ContactForm
from django.contrib import messages

def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            new_contact = Contactus(name=request.POST['name'], email=request.POST['email'], 
            phone=request.POST['phone'], message=request.POST['message'])
            new_contact.save()
            messages.success(request, 'We will contact u soon... :)')
            return redirect('contactus')
        else:
            messages.error(request, form.errors)
    else:
        form = ContactForm()

    return render(request, 'contactus/contactus.html', {'form': form})