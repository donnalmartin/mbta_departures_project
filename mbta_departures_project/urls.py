"""mbta_departures_project URL Configuration
"""

from django.conf.urls import include, url

urlpatterns = [
    url(r'', include('mbta_departures.urls')),
]