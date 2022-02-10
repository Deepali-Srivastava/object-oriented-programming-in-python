# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of Python course available on CourseGalaxy.com

class Person:
    species  = 'Homo sapiens'
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.count += 1

    def display(self):
         print(f'{self.name} is {self.age} years old')

    @classmethod
    def show_count(cls):
        print(f'There are {cls.count} {cls.species}')

Person.show_count()
p1 = Person('John',20)
p2 = Person('Jack',34)
Person.show_count() 
