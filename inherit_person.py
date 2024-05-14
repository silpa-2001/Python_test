class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def disp(self):
        print("My real name is ",self.fname, self.lname)

class Daughter(Person):
    def __init__(self,name):
        #super().__init__(fname="Silpa",lname="Anil")
        Person.__init__(self,fname="Silpa",lname="Anil")
        
        self.name=name
    def disp(self):
        super().disp()
        print("My pet name is ",self.name)

p=Daughter("Chinnu")
p.disp()