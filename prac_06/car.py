"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Represent a Car object."""
    # 6. add car name
    def __init__(self, car_name="", fuel=0):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.fuel = fuel
        self._odometer = 0
        self.car_name = car_name

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
            self._odometer += distance
        return distance

    # 5.add the __str__ method to the Car class in car.py
    def __str__(self):
        return f"{self.car_name}, fuel = {self.fuel}, odometer = {self._odometer}"
