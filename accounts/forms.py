from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'placeholder':"First Name"}), required = True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'placeholder':"Last Name"}), required = True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'placeholder':"Username"}), required = True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control",'placeholder':"Email"}), required = True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Password"}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Confirm Password"}), required=True)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']
