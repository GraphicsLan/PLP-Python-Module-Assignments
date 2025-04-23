class Vehicle:
    def move(self):
        
        raise NotImplementedError("Subclasses must implement this method.")

class Car(Vehicle):
    def move(self):
    
        return "Driving " #Defines how the car moves

class Plane(Vehicle):
    def move(self):
        
        return "Flying " #Defines how the plane moves

class Boat(Vehicle):
    def move(self):
       
        return "Sailing " 


if __name__ == "__main__":
    
    car = Car()
    plane = Plane()
    boat = Boat()

    # polymorphism
    vehicles = [car, plane, boat]
    for vehicle in vehicles:
        print(vehicle.move())