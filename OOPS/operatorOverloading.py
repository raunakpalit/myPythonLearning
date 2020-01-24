class Student():
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        x = Student(m1, m2)
        return x

    def __gt__(self, other):
        x1 = self.m1 + self.m2
        x2 = other.m1 + other.m2
        if x1 > x2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(60, 69)
s2 = Student(79, 75)

# s3 = s1 + s2      # s3.__add__(s1, s2)
# print(s3.m1)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

print(s1)
print(s2)
