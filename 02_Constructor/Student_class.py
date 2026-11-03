class student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age =age
        self.grade = grade

student1 = student("John", 15, "A+") 
student2 = student("Alice", 14, "B+") 
student3 = student("Bob", 16, "A")

print(f"Student 1: Name - {student1.name}, Age - {student1.age}, Grade - {student1.grade}")
print(f"Student 2: Name - {student2.name}, Age - {student2.age}, Grade - {student2.grade}")
print(f"Student 3: Name - {student3.name}, Age - {student3.age}, Grade - {student3.grade}")

