class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def honk(self):
        print("Beep beep!")


my_car = Car('Toyota', 'Maroon')

print(my_car.brand)
print(my_car.color)



print(f"The brand of my car is {my_car.brand} while the color of it is {my_car.color}.")
my_car.honk()