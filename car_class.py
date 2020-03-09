# import my vehicle class
from vehicle_class import *

# define car class here and make it inherit from vehicle
class car(vehicle):
    def __init__(self, brand, horsepower, max_speed):
        self.brand = brand
        self.horse_power = horsepower
        self.max_speed = max_speed

    def park(self):
        return 'BEEP BEEP BEEP'

    def honk(self):
        return 'HONK HONK'

#Characterists:
# brand
# horse_power
# max_speed

#methods :
# park
# honk