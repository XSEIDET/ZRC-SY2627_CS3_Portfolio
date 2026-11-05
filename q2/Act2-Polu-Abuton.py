# 1. 
# a. Duck typing in python is a coding rule, 
#    if an object has the method you need, 
#    Python will use it. It cares about what the object can do,
#    not what its class inheritance is.
# b. It just needed to have the exact same method name, which is move().

# 2. Code

class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

if __name__ == "__main__":
    car = Car()
    boat = Boat()
    drone = Drone()

    start_trip(car)
    start_trip(boat)
    start_trip(drone)

# 3. The code demonstrates polymorphism because the same function (start_trip) 
#    can take entirely different vehicles and run their specific move() 
#    action using the exact same line of code.
