from rest_framework import serializers
from listings.models import Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'title', 'action_type', 
        'property_type', 'realtor', 'photo_main', 
        'city', 'location', 'address', 'price', 
        'bedrooms', 'bathrooms', 'built_up_area', 
        'carpet_area', 'unit', 'transaction_type', 
        'property_floor', 'ownership', 'total_floors', 
        'availability', 'description', 'posting_date']