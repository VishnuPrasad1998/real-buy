from django.contrib import admin
from .models import Shortlist
from import_export.admin import ImportExportModelAdmin

@admin.register(Shortlist)
class ShortlistAdmin(ImportExportModelAdmin):
    pass