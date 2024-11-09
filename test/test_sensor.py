import unittest

from car_park import CarPark
from sensor import EntrySensor

class TestSensor(unittest.TestCase):

    def setUp(self):
        self.car_id = 1
        self.is_active = True
        self.car_park = CarPark("Test Street 123", 100)
        self.sensor = EntrySensor(self.car_id, self.is_active, self.car_park)

    def test_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.sensor, EntrySensor)
        self.assertIsInstance(self.sensor.car_park, CarPark)
        self.assertEqual(self.sensor.id, 1)
        self.assertEqual(self.sensor.is_active, True)

    def test_sensor_detect_vehicle(self):
        self.sensor.detect_vehicle("TEST")
        self.assertEqual(self.sensor.plate, "TEST")