from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from realtors.models import Realtor
from django.contrib.auth.models import Group
import re

def registerPage(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        name = first_name + last_name 
        role = request.POST['role'] 
        role = int(role)
        print(role, type(role))
        if(role==2):
            print("Leven Realtor aan ketta")
            if password1 == password2:
          # Check username
                if User.objects.filter(username=username).exists():
                    return redirect('register')
                else:
                    if User.objects.filter(email=email).exists():
                        return redirect('register')
                    else:
                        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password1, email=email)
                        user.save()
                        group = role
                        user.groups.add(group)
                        realtor = Realtor(name=name, first_name=first_name, last_name=last_name, username=username, email=email)
                        realtor.save()
                        return redirect('login')
              
            else:
                return redirect('register')
        else:
            print("Leven User aan ketta")
        #Check if password match
            if password1 == password2:
          # Check username
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Person with same username does exist")
                    return redirect('register')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.info(request, "Person with same email does exist")
                        return redirect('register')
                    else:
                        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password1, email=email)
                        user.save()
                        group = role
                        user.groups.add(group)
                        return redirect('login')
              
            else:
                messages.info(request, "Password doesnot match")
                return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def loginPage(request):
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
                if(user.groups.all()[0].name == "Realtor"):
                    return redirect('dashboard_realtor')
                else:
                    return redirect('dashboard_user')

            else:
                messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def dashboard_realtor(request):
    return render(request, 'accounts/realtor_dashboard.html')

def dashboard_user(request):
    return render(request, 'accounts/user_dashboard.html')
