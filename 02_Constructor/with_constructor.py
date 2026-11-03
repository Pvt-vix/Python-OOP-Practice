class car():

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = car("Toyota", "Red") #Creating an object of the car class and passing the brand and color as arguments to the constructor

car2 = car("Honda", "Blue") #creating another object of the car class and passing the brand and color as arguments to the constructor

print(f"Car 1: Brand - {car1.brand}, Color - {car1.color}") 

print(f"Car 2: Brand - {car2.brand}, Color - {car2.color}") 
