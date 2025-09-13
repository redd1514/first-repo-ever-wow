print("\nActivity 1")
print("Welcome to Grade Manager!")
print("*******************************");


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    def average (self):
        return sum(self.grades) / len(self.grades)

category_grade = lambda avg: (
    "A" if avg >= 90 else
    "B" if avg >= 80 else
    "C" if avg >= 70 else
    "D" if avg >= 60 else
    "F"
)

name = input("\nEnter student's name: ")
grade1 =  float(input("Enter grade 1: "))
grade2 =  float(input("Enter grade 2: "))
grade3 =  float(input("Enter grade 3: "))

student = Student(name, [grade1, grade2, grade3])

avg = student.average()
category = category_grade(avg)

print(f"Student name: {student.name}")
print(f"Average grade: {avg:.2f}")
print(f"Category: {category}")
