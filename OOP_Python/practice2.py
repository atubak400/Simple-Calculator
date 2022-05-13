class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):
        return self.grade



class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        print ("Maximum number of student exceeded!!")

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()  # or student.grade

        return value / len(self.students)



Curry = Student("Steph Curry", 19, 95)
Klay = Student("Klay Thompson", 19, 75)
Poole = Student("Jordan Poole", 19, 65)
        
course = Course("Science", 2)
course.add_student(Curry)
course.add_student(Klay)
course.add_student(Poole)

print("Average Grade is ")
print(course.get_average_grade())

