from django.shortcuts import render
from django.views.generic import ListView
from listings.models import Listing
import json
# Create your views here.

class InfoListView(ListView):
    model = Listing
    template_name = 'listings/searchfast.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs_json"] = json.dumps(list(Listing.objects.values('title','city','location')))
        return context
    