# class variables => Shared among all instances of a class
#                 => They are defined outside the constructor
#                 => Allow you to share data among all objects created from a class

class Student:

    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student(name="Alice", age=20)
student2 = Student(name="Bob", age=22)
student3 = Student(name="Charlie", age=21)
student4 = Student(name="David", age=23)

print(student1.name) 
print(student1.age)
print(student1.class_year)

print(student2.name)  
print(student2.age)
print(Student.class_year)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students!")  # 2 students are created   