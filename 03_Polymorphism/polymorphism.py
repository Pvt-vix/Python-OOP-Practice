#Polymorphism with classes method overriding

#Defination of Polymorphism:
# Polymorphism is a concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). In Python, polymorphism can be achieved through method overriding, where a subclass provides a specific implementation of a method that is already defined in its superclass.

class Animal:
    def sound(self):
        print("Elephant sounds trumpet trumpet")


class Lion(Animal):
    def sound(self):
        print("lion sounds roar roar")

class Tiger(Animal):
    def sound(self):
        print("tiger sounds grrr grrr")


animal1 = Animal()
animal2 = Lion()
animal3 = Tiger()

animal1.sound()
animal2.sound()
animal3.sound()

