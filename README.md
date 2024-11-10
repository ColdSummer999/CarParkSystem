# MoonLander Car park system

![MoonLanderImage](images/new_car_park.png)

Monitors vehicle entry and exit, and displays real-time parking availability.

Key Components:

 - Parking Bays
 - Sensor Network
 - Digital Display

The script is written in python. Refer to `main.py` for example usages.

<a name="table-of-contents"></a>
## Table of Contents
> 1. [Documentation](#intro)
> 2. [Example](#example)

<a name="intro"></a>
## 1. Documentation

| Class Name | Attributes                                                 | Description                                                                                                                                                           | 
|------------|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CarPark    | location, capacity, plates, sensors,<br/>display, log_file | Car park object defines the location and capacity of the car park. Has a collection of displays and sensors to help track and display incoming and outgoing vehicles. | 
| Sensor     | id, is_active, car_park, plate                             | Continuously monitor vehicle traffic, capturing license plate numbers upon entry and exit. Transmit this data to the car park management system.                      |
| Display    | id, message, is_on, car_park                               | Display a message to incoming and outgoing vehicle.                                                                                                                   |


<a name="example"></a>
## 2. Example

```py
# Construct the car park, sensors and display
moon_land_car_park = CarPark("moondalup", 100, "moondalup.txt")
moon_land_entry_sensor = EntrySensor(1, True, moon_land_car_park)
moon_land_exit_sensor = ExitSensor(2, True, moon_land_car_park)
moon_land_displays = []

# Drive 10 cars into the car park
for car in range(10):
    moon_land_entry_sensor.detect_vehicle(f"TEST-PLATE-{car}")
    moon_land_displays.append(Display(car, moon_land_car_park, f"Welcome to Moondalup TEST-PLATE-{car}", True))
    print(moon_land_displays[car])

# 2 cars are leaving the car park
for car in range(2):
    moon_land_exit_sensor.detect_vehicle(f"TEST-PLATE-{car}")
    moon_land_displays[car].update({"message": "Goodbye!"})
    del moon_land_displays[car]
```



