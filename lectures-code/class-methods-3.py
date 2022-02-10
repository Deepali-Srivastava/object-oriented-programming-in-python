# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of Python course available on CourseGalaxy.com

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def from_str(cls,s):
        name,age = s.split(',')
        return cls(name, int(age))
        
    @classmethod
    def from_dict(cls,d):
        return cls( d['name'], d['age'] )

    def display(self):
         print('I am', self.name, self.age, 'years old')
         
p1 = Person('John', 20)
p2 = Person('Jim', 35)

s = 'Jack, 23'
d = {'name': 'Jane', 'age':34}
            
p3 = Person.from_str(s)
p3.display()

p4 = Person.from_dict(d)
p4.display()
 

