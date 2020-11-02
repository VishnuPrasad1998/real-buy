from django import forms
from .models import Contactus
from django.forms import ValidationError
import re  

class ContactForm(forms.ModelForm):
        class Meta:
            model = Contactus
            fields = ['name', 'email', 'phone', 'message']

        name = forms.CharField(max_length=100)
        email = forms.EmailField(max_length=100)
        phone = forms.CharField(max_length=100)
        message = forms.CharField(max_length=500)

        def clean(self):
            cleaned_data = super(ContactForm, self).clean()
            name = self.cleaned_data.get('name')
            email = self.cleaned_data.get('email')
            phone = self.cleaned_data.get('phone')
            print(type(phone))
            message = self.cleaned_data.get('message')
            if((len(name) == 0) and len(email) == 0 and len(message)==0 and len(phone)==0):
                raise forms.ValidationError("Form is Empty fill all fields ")
            if((len(name) < 3 or len(name) > 100)):
                raise forms.ValidationError("Name must be minimum 3 characters and maximum 100 characters")
            if(re.search("@gm(ai)l.com$", email)):
                print("Validemail")
            else:
                raise forms.ValidationError("Invalid Email address")
            if(len(phone) != 10):
                raise forms.ValidationError("Numbers field should contain 10 digit numbers")
            if(len(message) < 4 or len(message) > 500):
                raise forms.ValidationError("In Description Enter minimum 4 characters and max 500 characters")
            
        