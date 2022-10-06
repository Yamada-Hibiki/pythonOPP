# Object oriented programming
class Student:
    def __init__(self, name, age, grade):    # This gets called each time we instantiate
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        # create a method to add students to this course
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False

    def get_average(self):
        value = 0
        for student in self.students:
            value += student.get_grade()  # we don't put student.grade, so we will be able to modify his grade after
        return value / len(self.students)


s1 = Student("Tim", 19, 95)
s2 = Student("Tam", 19, 75)
s3 = Student("Tom", 19, 65)

course1 = Course("Science", 2)
course2 = Course("PE", 3)

course2.add_student(s1)
course2.add_student(s2)
course2.add_student(s3)
print(course2.students[1].name)
print(course2.get_average())
