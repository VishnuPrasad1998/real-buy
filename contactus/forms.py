from django import forms
from .models import Contactus
from django.forms import ValidationError
import re  

class ContactForm(forms.ModelForm):
        class Meta:
            model = Contactus
            fields = ['name', 'email', 'phone', 'message']

        name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'placeholder':"Name"}), required = False)
        email = forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control",'placeholder':"Email"}), required = False)
        phone = forms.CharField(required = False, widget=forms.TextInput(attrs={'class':"form-control",'placeholder':"Phone number"}))
        message = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control",'placeholder':"Message", 'rows':6, 'style':"background-color:#161616"}), required = False)
        
        def clean(self):
            cleaned_data = super(ContactForm, self).clean()
            name = self.cleaned_data.get('name')
            email = self.cleaned_data.get('email')
            phone = self.cleaned_data.get('phone')
            message = self.cleaned_data.get('message')
            if((len(name) == 0) and len(email) == 0 and len(message)==0 and len(phone)==0):
                raise forms.ValidationError("Form is Empty fill all fields ")
            if((len(name) < 3 or len(name) > 100)):
                self.add_error(None, ValidationError("Name must be minimum 3 characters and maximum 100 characters"))
            if(re.search("@gm(ai)l.com$", email)):
                print("Validemail")
            else:
                self.add_error(None, ValidationError("Invalid email address"))
            if(len(phone) != 10):
                self.add_error(None, ValidationError("Ten digits mandatory"))
            if(len(message) < 4 or len(message) > 500):
                self.add_error(None, ValidationError("In Description Enter minimum 4 characters and max 500 characters"))
            
        