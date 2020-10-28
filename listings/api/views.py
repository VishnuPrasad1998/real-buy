from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from listings.models import Listing
from listings.api.serializers import ListingSerializer

def index(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Listing.objects.all()
        serializer = ListingSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)