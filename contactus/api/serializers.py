from rest_framework import serializers
from contactus.models import Contactus

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactus
        fields = ['id', 'name', 'email', 
        'phone', 'message', 'contact_date']
