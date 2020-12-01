from import_export import resources
from .models import Shortlist

class ShortlistResource(resources.ModelResource):
    class Meta:
        model = Shortlist