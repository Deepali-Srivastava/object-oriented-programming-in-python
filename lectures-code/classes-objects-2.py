# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of Python course available on CourseGalaxy.com

class Person:
    def set_details(self,name,age):
        self.name = name
        self.age = age
        
    def display(self):
         print('I am',self.name)
         
    def greet(self):
        if self.age < 80:
            print('Hello, how are you doing?')
        else:
            print('Hello, How do you do ?')
        self.display()

    def get_old(self):
        self.age = 75

        
p1 = Person()
p2 = Person()

p1.set_details('John',20)
p2.set_details('Jack',90)

p1.greet()
p2.greet()

p1.get_old()
print(p1.age)


