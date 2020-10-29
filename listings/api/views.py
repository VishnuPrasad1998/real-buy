from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from listings.models import Listing
from listings.api.serializers import ListingSerializer

class PropertyListing(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Listing.objects.all()
        serializer = ListingSerializer(snippets, many=True)
        return Response(serializer.data)