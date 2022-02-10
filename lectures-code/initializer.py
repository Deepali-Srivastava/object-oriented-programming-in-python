# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of Python course available on CourseGalaxy.com

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display(self):
         print('I am',self.name)
         
    def greet(self):
        if self.age < 80:
            print('Hello, how are you doing?')
        else:
            print('Hello, How do you do ?')

p1=Person('John',20)
p2=Person('Jack',90)

p1.display()
p1.greet()

p2.display()
p2.greet()



