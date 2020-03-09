# define vehicle class here

class vehicle():
    def __init__(self, n_passengers, size_cargo):
        self.n_passengers = n_passengers
        self.size_cargo = size_cargo

    def accelerate(self):
        return 'ZOOM'

    def brake(self):
        return 'BRAKE'

#Characteristics:
# n_passengers
# size_cargo

#methods:
# accelerate