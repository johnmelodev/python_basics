# example
class Car:
    def start(self):
        print('Starting the car')


class Motorcycle:
    def start(self):
        print('Starting the motorcycle')


def start(vehicle):
    vehicle.start()


# Usage example
car = Car()
motorcycle = Motorcycle()

start(car)
start(motorcycle)