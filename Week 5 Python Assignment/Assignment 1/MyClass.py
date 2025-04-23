class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def start_engine(self):
        return f"The {self.color} {self.brand} {self.model} is starting its engine."

    def stop_engine(self):
        return f"The {self.color} {self.brand} {self.model} has stopped its engine."

    def drive(self):
        return f"The {self.color} {self.brand} {self.model} is driving."

class ElectricCar(Car):
    def __init__(self, brand, model, year, color, battery_capacity):
        super().__init__(brand, model, year, color)
        self.battery_capacity = battery_capacity

    def charge_battery(self):
        return f"The {self.color} {self.brand} {self.model} is charging its {self.battery_capacity}kWh battery."

    def drive(self):  # Overrides Car.drive
        return f"The {self.color} {self.brand} {self.model} is driving silently with electric power."

if __name__ == "__main__":
    car = Car("Toyota", "Corolla", 2020, "red")
    print(car.start_engine())
    print(car.drive())
    print(car.stop_engine())

    tesla = ElectricCar("Tesla", "Model S", 2023, "blue", 100)
    print(tesla.start_engine())
    print(tesla.drive())
    print(tesla.charge_battery())
