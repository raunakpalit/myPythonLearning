class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.stream = None

    def student_details(self):
        return "Student Name: {} \nStudent Age: {} \nGender: {}".format(self.name, self.age, self.gender)

    def set_stream(self, stream):
        self.stream = stream

    def get_stream(self):
        return self.stream

class College(Student):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def update_stream(self, stream):
        super().set_stream(stream)

raunak = College('Raunak', 34, 'Male')
print(raunak.student_details())
raunak.update_stream('Electronics')
print(raunak.get_stream())



