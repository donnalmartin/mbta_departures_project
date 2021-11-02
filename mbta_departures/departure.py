import datetime

def parse_return(str, default=''):
    try:
        return str[:25].upper()
    except:
        return default

class Departure():
    
    def __init__(self, carrier, arrival_time, departure_time, destination,
                 train, track, status):
        self.carrier = parse_return(carrier, 'MBTA')
        self.arrival_time = parse_return(arrival_time)
        self.departure_time = parse_return(departure_time)
        self.destination = parse_return(destination)
        self.train = parse_return(train)
        self.track = parse_return(track, 'TBD')
        self.status = parse_return(status, 'ON TIME')
    
    def time(self):
        try:
            dt = datetime.datetime.strptime(self.departure_time, '%Y-%m-%dT%H:%M:%S%z')
            return dt.strftime('%I:%M %p')
        except:
            return ''