class department:
    def __init__(self):
        self.levels = list()
    def y(self, other,x,y):
        level = other( x, y)
        self.levels.append(level)

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

m = department()
m.y(levels,'one','seconde term')
m.y(levels,'two','first term')
m.y(levels,'three','first term')
m.y(levels,'four','first term')
m.y(levels,'five','first term')
m.y(levels,'six','first term')

m.levels[0].x(students,'a',12)
m.levels[0].x(students,'b',12)
m.levels[0].x(students,'c',12)
m.levels[0].x(students,'d',12)
m.levels[0].x(students,'e',12)

m.levels[1].x(students,'f',12)
m.levels[1].x(students,'g',12)
m.levels[1].x(students,'h',12)
m.levels[1].x(students,'i',12)
m.levels[1].x(students,'j',12)
m.levels[1].x(students,'k',12)

m.levels[2].x(students,'k',12)
m.levels[2].x(students,'k',12)
m.levels[2].x(students,'k',12)
m.levels[2].x(students,'k',12)
m.levels[2].x(students,'k',12)
m.levels[2].x(students,'k',12)
m.levels[2].x(students,'k',12)
m.levels[2].x(students,'k',12)
m.levels[2].x(students,'k',12)



for i in m.levels:
    print ('\n___________\n')
    print (i.level)
    counter = 0
    for j in i.student:
        counter +=1
        print ('\n______________')
        print ("student ",counter , ':')
        print ("name ",j.name)
        print ("age:",j.age)
      