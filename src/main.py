from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

# TODO: create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
# TODO: create an entry sensor object with id 1, is_active True, and car_park car_park
# TODO: create an exit sensor object with id 2, is_active True, and car_park car_park
# TODO: create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
# TODO: drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
# TODO: drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)

"""
    Code to simulate car park system.
        * Create car park object.
        * Create entry and exit sensor and display object.
        * Drive 10 cars into the car park which gets triggered via the sensor
        * Drive 2 cars out of the car park

    The CarPark class supports saving the setting into a config file.
    @methods:
        CarPark.write_config()
            to save setting to config file
        CarPark.read_config()
            to read config file
"""

if __name__ == '__main__':
    # Construct the car park, sensors and display
    moon_land_car_park = CarPark("moondalup", 100, "moondalup.txt")
    moon_land_entry_sensor = EntrySensor(1, True, moon_land_car_park)
    moon_land_exit_sensor = ExitSensor(2, True, moon_land_car_park)
    moon_land_display = Display(1, moon_land_car_park, "Welcome to Moondalup", True)

    """
        moon_land_car_park.write_config()
        another_moon_land = CarPark.from_config()
        print(another_moon_land.capacity)
    """

    # Drive 10 cars into the car park
    for car in range(10):
        moon_land_entry_sensor.detect_vehicle(f"TEST-PLATE-{car}")

    # 2 cars are leaving the car park
    for car in range(2):
        moon_land_exit_sensor.detect_vehicle(f"TEST-PLATE-{car}")