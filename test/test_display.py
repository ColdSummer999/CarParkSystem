import unittest
from display import Display
from car_park import CarPark


class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("Example 123 street", 100)
        self.display_id = 1
        self.message = {"message": "Welcome to the car park"}
        self.is_on = True
        self.display = Display(self.display_id, self.car_park, self.message, self.is_on)

    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.message, {"message": "Welcome to the car park"})
        self.assertEqual(self.display.is_on, True)
        self.assertIsInstance(self.display.car_park, CarPark)

    def test_update(self):
        self.display.update({"message": "GoodBye"})
        self.assertEqual(self.display.message, {"message": "GoodBye"})


if __name__ == '__main__':
    unittest.main()
