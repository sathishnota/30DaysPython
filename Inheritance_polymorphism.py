# Parent class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show(self):
        print("This is a car:", self.brand, self.model)

# Child class
class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)  # Get brand and model from Car
        self.battery = battery

    # Overriding the show method
    def show(self):
        print("This is an electric car:", self.brand, self.model, "- Battery:", self.battery, "kWh")

# Using the classes
car1 = Car("Toyota", "Camry")
ecar1 = ElectricCar("Tesla", "Model Y", 75)

car1.show()     # Uses Car's show
ecar1.show()    # Uses ElectricCar's show (polymorphism)
