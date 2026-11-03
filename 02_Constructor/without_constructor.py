#code Without Constructors 

class car:
    def set_details(self,brand,color):
        self.brand = brand
        self.color = color

car1 = car()
car1.set_details("Toyota", "Red")

car2 = car()
car2.set_details("Honda", "Blue")

print(f"Car 1: Brand - {car1.brand}, Color - {car1.color}")
print(f"Car 2: Brand - {car2.brand}, Color - {car2.color}")
