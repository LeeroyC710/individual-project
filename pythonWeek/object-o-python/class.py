class Student():
    def __init__(self, maths, english, science):
        self.maths = maths
        self.english = english
        self.science = science

    def get_average(self):
        average_score = (self.maths + self.english + self.science)/3
        return average_score

student = Student(80, 66, 77)
average = student.get_average()
print(average)

student2 = Student(61, 92, 53)
average = student2.get_average()
print(average)

