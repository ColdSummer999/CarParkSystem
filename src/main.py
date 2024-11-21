from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display


if __name__ == '__main__':
    # Construct the car park, sensors and display
    moon_land_car_park = CarPark("moondalup", 100, "moondalup.txt")
    moon_land_entry_sensor = EntrySensor(1, True, moon_land_car_park)
    moon_land_exit_sensor = ExitSensor(2, True, moon_land_car_park)
    moon_land_car_park.add_sensor(moon_land_entry_sensor)
    moon_land_car_park.add_sensor(moon_land_exit_sensor)

    # Drive 10 cars into the car park
    for car in range(10):
        moon_land_entry_sensor.detect_vehicle(f"TEST-PLATE-{car}")
        moon_land_car_park.add_display(Display(car, moon_land_car_park,
                                               {"message": "Welcome to moon land car park."}, True))
        print(moon_land_car_park.displays[car])

    # 2 cars are leaving the car park
    for car in range(2):
        moon_land_exit_sensor.detect_vehicle(f"TEST-PLATE-{car}")
        moon_land_car_park.displays[car].update({"message": "Goodbye!"})
        print(moon_land_car_park.displays[car])
        moon_land_car_park.remove_display(car)

