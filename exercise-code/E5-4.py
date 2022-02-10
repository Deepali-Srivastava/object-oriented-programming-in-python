# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of Python course available on CourseGalaxy.com

class Person:
    def __init__(self,id):
        self.id = id
        
class Teacher(Person):
    def __init__(self,id):
        super().__init__(id)
        self.id += 'T'
    
class Student(Person):
    def __init__(self,id):
        super().__init__(id)
        self.id += 'S'
   
class TeachingAssistant(Student, Teacher):
     def __init__(self,id):
        super().__init__(id)
        
   
x = TeachingAssistant('2675')
print(x.id)
y = Student('4567')
print(y.id)
z = Teacher('3421')
print(z.id)
p = Person('5749')
print(p.id)
