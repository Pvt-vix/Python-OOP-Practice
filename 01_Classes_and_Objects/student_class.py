class Student:
    def set_details(self,name,age,roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def see_details(self):
        print(f"student is {self.name}, and the age is {self.age}, and the roll number is {self.roll_no}")

class1 = Student() 
class1.set_details("John", 20, 101)

class2 = Student()
class2.set_details("Alice", 22, 102)

class1.see_details()
class2.see_details()    