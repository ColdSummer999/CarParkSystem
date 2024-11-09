

from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime


class CarPark:
    def __init__(self, location, capacity, log_file=Path("log.txt"), plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        # create the file if it doesn't exist:
        self.log_file.touch(exist_ok=True)

    def __str__(self):
        # Return a string that contain the car park's location and capacity
        return f"Location : { self.location }, capacity: { self.capacity }"

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Not a Sensor or Display")
        elif isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        # Add plate number and update the display
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        # Remove the plate number and update the display
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")

    @property
    def available_bays(self):
        bays_available = self.capacity - len(self.plates)
        return 0 if bays_available <= 0 else bays_available

    def update_displays(self):
        data = {"available bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(data)

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")
