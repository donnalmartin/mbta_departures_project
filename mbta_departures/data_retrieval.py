import requests, json

API_URL = 'https://api-v3.mbta.com/'
KEY = '12e084774c254ac28168b211e3c2da1d'

def get_api_data (req, params):
   params.update({'api_key':KEY})
   r = requests.get(API_URL + req,
                    params=params)
   if r.status_code == 200:
       return json.loads(r.text)['data']
   else:
       print("Status code " + str(r.status_code) + " returned for " + req + " call.")

def get_stations():
    stations = []
    stations_return = get_api_data('stops', {'filter[location_type]':1})
    if stations_return:
        for station in stations_return:
            station_attributes = station['attributes']
            station_attributes.update({'id':station['id']})
            stations.append(station_attributes)
    return stations

def get_station(stationId):
    stations = get_api_data('stops', {'id':stationId,
                                      'include':'child_stops'})
    if stations:
        return stations[0]

def get_routes(stationId):
    return get_api_data('routes', {'filter[stop]':stationId})

def get_predictions(stationId):
    return get_api_data('predictions',
                        {'filter[stop]':stationId})

def get_trip(tripId):
    trips = get_api_data('trips', {'id':tripId})
    if trips:
        return trips[0]

def get_vehicle(vehicleId):
    return get_api_data('vehicles', {'id':vehicleId})