from .data_retrieval import get_station, get_predictions, get_trip, get_vehicle
from .departure import Departure

def get_trip_destination(trip):
    if trip:
        return trip['attributes']['headsign']

def get_prediction_destination(prediction):
    if prediction:
        trip_data = prediction['relationships']['trip']['data']
        if trip_data:
            trip_id = trip_data['id']
            return get_trip_destination(trip_id)

def get_prediction_trip(prediction):
    if prediction:
        trip_data = prediction['relationships']['trip']['data']
        if trip_data:
            trip_id = trip_data['id']
            return get_trip(trip_id)
        
def get_prediction_vehicle(prediction):
    if prediction:
        vehicle_data = prediction['relationships']['vehicle']['data']
        if vehicle_data:
            vehicle_id = vehicle_data['id']
            vehicles = get_vehicle(vehicle_id)
            if vehicles:
                return vehicles[0]

def get_vehicle_label(vehicle):
    if vehicle:
        return vehicle['attributes']['label']

def generate_departures(station_id):
    departures = []
    station = get_station(station_id)
    if station:
        stops = station['relationships'].get('child_stops')
        if stops:
            for stop_reference in stops['data']:
                stop_id = stop_reference['id']
                stop = get_station(stop_id)
                stop_attributes = stop['attributes']
                # vehicle type of 2 indicates Commuter Rail
                if stop_attributes['vehicle_type'] == 2:
                    track = stop_attributes['platform_code']
                    predictions = get_predictions(stop_id)
                    if predictions:
                        for prediction in predictions:
                            prediction_attributes = prediction['attributes']
                            arrival_time = prediction_attributes['arrival_time']
                            departure_time = prediction_attributes['departure_time']
                            # departure_time of None indicates riders will not be able to board
                            if departure_time:
                                trip = get_prediction_trip(prediction)
                                destination = get_trip_destination(trip)
                                vehicle = get_prediction_vehicle(prediction)
                                train = get_vehicle_label(vehicle)
                                status = prediction_attributes['status']
                                carrier = None
                                departure = Departure(carrier, arrival_time, 
                                                      departure_time, destination,
                                                       train, track, status)
                                departures.append(departure)
    return departures