# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of Python course available on CourseGalaxy.com

class Person:
    def greet(self):
        print('I am a Person')

class Teacher(Person):
    def greet(self):
        Person.greet(self)    
        print('I am a Teacher')

class Student(Person):
    def greet(self):
        Person.greet(self)    
        print('I am a Student')

class TeachingAssistant(Student, Teacher):
     def greet(self):
         Student.greet(self)
         Teacher.greet(self)
         print('I am a Teaching Assistant')
       
x = TeachingAssistant()
x.greet()
 
