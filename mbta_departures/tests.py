from django.test import TestCase
from .departure import Departure

class DepartureTestCase(TestCase):
    @classmethod
    def setUpTestData(self):
        self.standardDeparture = Departure('carrier1', '2021-11-01T01:20:30-04:00',
                                           '2021-11-01T02:20:30-04:00', 'NORTH STATION',
                                           '01', '2', 'BOARDING')
        self.oddDeparture = Departure(None, None, '2021-11-01T01:20:30', 'NoRtH StAtIoN',
                                      'Track01', None, None)
    
    def setUp(self):
        pass
    
    def test_provided_carrier(self):
        self.assertEqual(self.standardDeparture.carrier, 'CARRIER1')
        
    def test_default_carrier(self):
        self.assertEqual(self.oddDeparture.carrier, 'MBTA')
    
    def test_properly_formatted_time(self):
        self.assertEqual(self.standardDeparture.time(), '02:20 AM')
        
    def test_improperly_formatted_time(self):
        self.assertEqual(self.oddDeparture.time(), '')
    
    def test_default_arrival_time(self):
        self.assertEqual(self.oddDeparture.arrival_time, '')
    
    def test_destination_formatting(self):
        self.assertEqual(self.oddDeparture.destination, 'NORTH STATION')
    
    def test_default_track(self):
        self.assertEqual(self.oddDeparture.track, 'TBD')
    
    def test_default_status(self):
        self.assertEqual(self.oddDeparture.status, 'ON TIME')