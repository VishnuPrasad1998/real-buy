"""realbuy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from quicksearch.views import InfoListView

urlpatterns = [
    #URL Patterns for rest api's
    path('api/listings', include('listings.api.urls')),
    path('api/contactus', include('contactus.api.urls')),
    path('api/accounts', include('accounts.api.urls')),

    

    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('contactus/', include('contactus.urls')),
    path('accounts/', include('accounts.urls')),
    path('visualization/', include('visualization.urls')),
    path('quicksearch/', InfoListView.as_view(), name='quicksearch'),
    path('shortlist/', include('shortlist.urls')),
    path('accounts/social/', include('allauth.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
