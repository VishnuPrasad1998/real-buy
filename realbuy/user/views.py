from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
import re

@login_required(login_url='login')
def home(request):
    return render(request, 'user/home.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for '+ user)
                return redirect('login')

        context = {'form':form}
        return render(request, 'user/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':

            email = request.POST.get('email')
            password = request.POST.get('password')

            #To check whether user input is Mailid or Username
            if(re.search("@gmail.com$", email)):
                user_list = User.objects.filter(email=email)
                for val in user_list:
                    user = authenticate(request, username=val.username, password=password)
            else:
                user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'user/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')