
import unittest
from pathlib import Path
from car_park import CarPark

DEBUG = False


class TestCarPark(unittest.TestCase):

    def setUp(self):
        self.log_path = Path("new_log.txt")
        self.car_park = CarPark("123 Example Street", 100, self.log_path)

    def test_car_park_initialized_with_all_attributes(self):
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.sensors, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)
        self.assertEqual(self.car_park.log_file, self.log_path)

    def test_add_car(self):
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.car_park.available_bays, 99)

    def test_remove_car(self):
        self.car_park.add_car("FAKE-001")
        self.car_park.remove_car("FAKE-001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 100)

    def test_overfill_the_Car_Park(self):
        for i in range(100):
            self.car_park.add_car(f"FAKE-{i}")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.add_car("FAKE-100")
        # Overfilling the car park should not change the number of available bays
        self.assertEqual(self.car_park.available_bays, 0)

        # Removing a car from an overfilled car park should not change the number of available bays
        self.car_park.remove_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)

    def test_removing_a_car_that_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.car_park.remove_car("NO-1")

    def test_register_raises_type_error(self):
        if DEBUG:
            self.test_car_park = CarPark("123 Example Street", 100)
            self.string_obj = ""
            self.test_car_park.register(self.string_obj)
        with self.assertRaises(TypeError):
            self.car_park.register("Not a Sensor or Display")

    def test_log_file_created(self):
        new_carpark = CarPark("123 Example Street", 100, self.log_path)
        self.assertTrue(self.log_path.exists())

    def tearDown(self):
        """
            Clean files that are created by this test unit.
        """
        self.log_path.unlink(missing_ok=True)

    def test_car_logged_when_entering(self):
        new_carpark = CarPark("123 Example Street", 100, self.log_path)
        self.car_park.add_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        # check plate entered
        self.assertIn("NEW-001", last_line)
        # check description
        self.assertIn("entered", last_line)
        # check entry has a new line
        self.assertIn("\n", last_line)

    def test_car_logged_when_exiting(self):
        new_carpark = CarPark("123 Example Street", 100, self.log_path)
        self.car_park.add_car("NEW-001")
        self.car_park.remove_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        # check plate entered
        self.assertIn("NEW-001", last_line)
        # check description
        self.assertIn("exited", last_line)
        # check entry has a new line
        self.assertIn("\n", last_line)


if __name__ == '__main__':
    unittest.main()
