
class Display:
    def __init__(self, id, car_park, message=None, is_on=False):
        self.id = id
        self.message = message or {}
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        # Print id and message.
        available_bays = self.message["available bays"]
        message = self.message["message"]
        temperature = self.message["temperature"]
        return f"Display {self.id}: {message} {available_bays} bays available. {temperature} degrees Celsius"

    def update(self, data):
        self.message = {**self.message, **data}
