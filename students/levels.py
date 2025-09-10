class levels:
    def __init__(self, level, term):
        self.level = level
        self.term = term
        self.student = list()
    def x(self,other,name, age):
        student = other(name, age)
        self.student.append(student)
class students:
    def __init__(self,name, age):
        self.name = name 
        self.age = age 

l = levels("first level","second term")
l.x(students, 'ali',19)
l.x(students, 'saleh',19)
l.x(students, 'khaled',19)
l.x(students, 'ahmed',19)
l.x(students, 'mohammed',19)

for n in l.student:
    print(n.name)
