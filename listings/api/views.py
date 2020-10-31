from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from listings.models import Listing
from listings.api.serializers import ListingSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

class PropertyListing(APIView):
    """
    GET and POST the whole properties
    """
    def get(self, request, format=None):
        snippets = Listing.objects.all()
        serializer = ListingSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListingDetails(APIView):
    """
    CRUD operation based on primary key
    """
    def get_object(self, pk):
        try:
            return Listing.objects.get(pk=pk)
        except Listing.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ListingSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ListingSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PropertyListFilters(ListAPIView):
    """
    API for filtering
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('city', 'price', 'bedrooms')
    
class FeaturedListings(APIView):
    """
    API for listings based on price
    """
    def get(self, request, format=None):
        featured_listings = Listing.objects.raw('SELECT * FROM listings_listing ORDER BY price DESC')
        serializer = ListingSerializer(featured_listings, many=True)
        return Response(serializer.data)

class RecentListings(APIView):
    """
    API for Top 6 listings based on listing time
    """
    def get(self, request, format=None):
        recent_listings = Listing.objects.raw('SELECT * FROM listings_listing ORDER BY posting_date DESC LIMIT 6')
        serializer = ListingSerializer(recent_listings, many=True)
        return Response(serializer.data)