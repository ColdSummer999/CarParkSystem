
from abc import ABC, abstractmethod
import random


class Sensor(ABC):
    def __init__(self, id, is_active, car_park, plate=None):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park
        self.plate = plate

    def __str__(self):
        return f"{self.id} is {'active' if self.is_active else 'not active'}"

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def detect_vehicle(self, plate=None):
        # Function that detect incoming vehicle, for now if vehicle return a plate, use the plate, otherwise
        # create a random one from our private method _scan_plate
        if plate is None:
            plate = self._scan_plate()
        self.plate = plate
        self.update_car_park(plate)

    def _scan_plate(self):
        return 'FAKE-' + format(random.randint(0, 999), "03d")


class EntrySensor(Sensor):

    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")


class ExitSensor(Sensor):
    def _scan_plate(self):
        return random.choice(self.car_park.plates)

    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚘 vehicle detected. Plate: {plate}")



