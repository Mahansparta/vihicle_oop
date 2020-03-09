from car_class import *
from plane_class import *

vehicle1 = vehicle(9, 'Big Family')
vehicle2 = vehicle(80, 'At least 80 bags')

# call methods and attributes to test

print(vehicle1.accelerate())
print(vehicle1.brake())
print(vehicle2.accelerate())
print(vehicle2.brake())
