# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of Python course available on CourseGalaxy.com

class MyClass():

     a = 5
     def  __init__(self, x):
          self.x = x
 
     def method1(self):
          print(self.x)

     @classmethod      
     def method2(cls):
          print(cls.a)

     @staticmethod
     def method3(m,n):
          retrun m+n     
 
