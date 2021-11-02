from django.db import models
from .data_retrieval import get_stations

def get_station_options():
    station_options = []
    for station in get_stations():
        station_options.append((station['id'], station['name'].upper()))
    return sorted(station_options,
                   key=lambda tup: tup[1])

class StationModel(models.Model):
    name = models.CharField(max_length=30,
                            choices=sorted(get_station_options(),
                                           key=lambda tup: tup[1]))