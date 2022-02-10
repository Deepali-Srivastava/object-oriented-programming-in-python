# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of Python course available on CourseGalaxy.com

class Teacher:
    def greet(self):
        print('I am a Teacher')

class Student:
    def greet(self):
        print('I am a Student')

class TeachingAssistant(Student, Teacher):
     def greet(self):
        print('I am a Teaching Assistant')
        
x = TeachingAssistant()
x.greet()

print(TeachingAssistant.__bases__) 
