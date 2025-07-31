class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"{self.name}, {self.age} yoshda.")

students = [
    Student("Ali", 15),
    Student("Laylo", 17),
    Student("Aziz", 14),
    Student("Diyora", 16),
    Student("Sardor", 18)
]


oldest_student = students[0]
for student in students[1:]:
    if student.age > oldest_student.age:
        oldest_student = student


oldest_student.show_info()
