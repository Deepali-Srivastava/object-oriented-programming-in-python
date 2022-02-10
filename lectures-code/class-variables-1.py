# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of Python course available on CourseGalaxy.com

class Person:
    species  = 'Homo sapiens'
    count = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.count+=1

    def display(self):
         print(f'{self.name} is {self.age} years old')
         
p1 = Person('John',20)
p2 = Person('Jack',34)

p1.display()
p2.display()

print(Person.count)
p3=Person('Jill', 40)
p4=Person('Jane', 35)
print(Person.count) 
