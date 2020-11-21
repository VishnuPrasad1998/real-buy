from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, ProfileForm
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from listings.models import Listing
from django.contrib.auth.decorators import login_required
import re

def registerPage(request):
    form = CreateUserForm(request.POST)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2'] 

        #Check if password match
        if password == password2:
      # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                else:
                    user = User.objects.create_user(first_name=first_name, username=username, password=password, email=email, last_name=last_name)
                    user.save()
                    UserProfile.objects.create(
                        user=user,
                    )
                    messages.success(request, 'Registered successfully...')
                    return redirect('login')
          
        else:
            messages.error(request, 'Passwords do not match')
    else:
        form = CreateUserForm()
    return render(request, 'accounts/register.html',{'form': form})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':

                email = request.POST.get('email')
                password = request.POST.get('password')
                print(email)
                #To check whether user input is Mailid or Username
                if(re.search("@gmail.com$", email)):
                    user_list = User.objects.filter(email=email)
                    print(user_list)
                    for val in user_list:
                        user = authenticate(request, username=val.username, password=password)
                else:
                    user = authenticate(request, username=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, "Logged out successfully...")
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    user = request.user
    listing_details = Listing.objects.filter(user__username__contains=user)
    context = {
        'listing_details': listing_details
    }
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def profileupdate(request):
    userprofile = request.user.userprofile
    form = ProfileForm(instance=userprofile)
    if  request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=userprofile)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form':form}
    return render(request, 'accounts/profile.html', context)