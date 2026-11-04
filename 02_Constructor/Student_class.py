class student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age =age
        self.grade = grade

student1 = student("John", 20, "A+") 
student2 = student("Alice", 14, "B+") 
student3 = student("Bob", 16, "A")

print(f"Student 1: Name - {student1.name}, Age - {student1.age}, Grade - {student1.grade}")
print(f"Student 2: Name - {student2.name}, Age - {student2.age}, Grade - {student2.grade}")
print(f"Student 3: Name - {student3.name}, Age - {student3.age}, Grade - {student3.grade}")

"""
1 -Default Constructor: A default constructor is a constructor that takes no arguments. It is used to create an object with default values. If no constructor is defined in a class, Python provides a default constructor.(self)

2 - Parameterized Constructor: A parameterized constructor is a constructor that takes arguments. It is used to create an object with specific values provided during object creation. In the example above, the constructor takes three parameters: name, age, and grade, which are used to initialize the attributes of the student class. (self, name, age, grade)

3 - constructor with default values (self, name="Unknown", age=0, grade="N/A"): A constructor with default values allows you to create an object without providing all the arguments. If some arguments are not provided, the default values will be used. For example, if you create a student object without specifying the name, age, or grade, it will use the default values defined in the constructor.
"""