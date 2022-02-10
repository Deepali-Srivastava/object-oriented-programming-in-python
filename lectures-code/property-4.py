# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of Python course available on CourseGalaxy.com

class Rectangle():
    def __init__(self,length,breadth):
           self.length = length
           self.breadth = breadth
    
    def area(self):
          return self.length * self.breadth

    def perimeter(self):
          return 2*(self.length + self.breadth)

    @property
    def diagonal(self):
          return (self.length*self.length + self.breadth * self.breadth)**0.5 

r = Rectangle(2,5)
print(r.diagonal)
r.length = 10
print(r.diagonal)


