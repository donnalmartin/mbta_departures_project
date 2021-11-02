import datetime
from .analyze_data import generate_departures

class Station():
    
    def __init__(self, id):
        self.id = id
        self.current_time =  ''
        
    def current_departures(self):
        self.current_time = datetime.datetime.now()
        departures = generate_departures(self.id)
        return sorted(departures,
                      key=lambda d: d.time())
        