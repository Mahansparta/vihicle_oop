# define vehicle class here
from vehicle_class import *

class Plane(vehicle):
    def __init__(self, passengers, cargo, airline, distance):
        super().__init__(passengers, cargo)
        self.airline = airline
        self.distance = distance


    def takeoff(self):
        return 'fly'

    def touchdown(self):
        return 'touchdown'

#Characteristics:
# n_passengers
# size_cargo

#methods:
# accelerate