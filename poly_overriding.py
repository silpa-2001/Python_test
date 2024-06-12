class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def disp(self):
        print("Name:",self.name,"\nAge:",self.age)
class Student(Person):
    def __init__(self,name,age,course):
        super().__init__(name,age)
        self.course=course

    def disp(self):
        super().disp()
        print("Course:",self.course)

class Teacher(Person):
    def __init__(self,name,age,subj):
        super().__init__(name,age)
        self.subj=subj

    def disp(self):
        super().disp()
        print("Subject:",self.subj)

s1=Student("Alex",23,"MCA")
t1=Teacher("Margustin", 56,"Science")
s1.disp()
t1.disp()