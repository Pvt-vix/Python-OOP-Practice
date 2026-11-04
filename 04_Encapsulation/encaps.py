# What is Encapsulation in Python?
# Encapsulation is one of the fundamental principles of object-oriented programming (OOP) that restricts direct access to an object's attributes and methods. It allows you to bundle data (attributes) and methods (functions) that operate on that data into a single unit, known as a class. By controlling access to the internal state of an object, encapsulation helps maintain the integrity of the data and prevents unintended interference from outside code.

#Example for private encapsulation in Python:

class Student:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def get_name(self):
        return self.__name  

    def set_name(self, name):
        self.__name = name  # Setter method to modify the private attribute

    def get_age(self):
        return self.__age  # Getter method to access the private attribute

    def set_age(self, age):
        self.__age = age  # Setter method to modify the private attribute


# Creating an instance of the Student class
std1 = Student("John", 20)
std2 = Student("Alice", 22)

# Accessing private attributes using getter methods
print(std1.get_name())  # Output: John
print(std1.get_age())   # Output: 20

# Modifying private attributes using setter methods
std1.set_name("Mike")
std1.set_age(21)
print(std1.get_name())  # Output: Mike
print(std1.get_age())   # Output: 21

