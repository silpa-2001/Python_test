class Animal:
    name=""
    def eat(self):
        print("I can eat")

class Dog(Animal):
    def eat(self):
        super().eat()
        print("I like to eat Bones")
    def disp(self):
        print("My name is ",self.name)

dog=Dog()
dog.name="Jaggu"
dog.disp()
dog.eat()