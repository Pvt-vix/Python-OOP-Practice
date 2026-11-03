class car:

    def set_details(self, brand, name, year):
        self.brand = brand
        self.name = name
        self.year = year

    def show_details(self):
         print(f"Car Brand: {self.brand}")
         print(f"Car Name: {self.name}")
         print(f"Car Year: {self.year}")

car1 = car()
car1.set_details("Toyota", "Camry", 2020)

car2 = car()
car2.set_details("Honda", "Civic", 2019)

car1.show_details()
car2.show_details()