from django import forms
from .models import Listing


class ListingModelForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
        exclude = ['user','posting_date']

class ListingEditModelForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
        exclude = ['user','posting_date']