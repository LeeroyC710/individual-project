class Student():
    english = 0
    maths = 0
    science = 0
    def get_average(self):
        return (self.english + self.maths + self.science) / 3

student_1 = Student()
student_1.english = 5
student_1.maths = 6
student_1.science = 7
print(student_1.get_average())


