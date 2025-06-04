class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def display(self):
        print(f"Car Details:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")


my_car = Car("Toyota", "Camry", 2019, "Black")
my_car2 = Car("BMW","X7",2022,"White")
my_car.display()
my_car2.display()
