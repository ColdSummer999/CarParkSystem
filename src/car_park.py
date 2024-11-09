

from sensor import Sensor
from display import Display


class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        # Return a string that contain the car park's location and capacity
        return f"Location : { self.location }, capacity: { self.capacity }"

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        elif isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        # Add plate number and update the display
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        # Remove the plate number and update the display
        self.plates.remove(plate)
        self.update_displays()

    @property
    def available_bays(self):
        bays_available = self.capacity - len(self.plates)
        return 0 if bays_available <= 0 else bays_available

    def update_displays(self):
        data = {"available bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(data)
