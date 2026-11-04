class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

dog  = Dog()
dog.speak()
dog.sound()

