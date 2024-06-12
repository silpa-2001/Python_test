class Animal:
    def __init__(self,name,food):
        self.name=name
        self.food=food
    
    def disp(self):
        print(self.name,"eats", self.food)

class Dog(Animal):
    def __init__(self, name, food):
        super().__init__(name, food)
    def hobby(self):
        print(self.name,"likes to play")

x= Dog("Jack","Bones")
x.disp()
x.hobby()
