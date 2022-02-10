# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of Python course available on CourseGalaxy.com

class Product:
    def __init__(self,x,y):
        self._x = x
        self._y = y
        
    def display(self):
        print(self._x, self._y)
    
    @property
    def value(self):
          return self._x

    @value.setter
    def value(self, val):
         self._x = val
    
    @property
    def y(self):
         return self._y
 
    @y.setter
    def y(self, val):
         self._y = val



p = Product(12,24)
print(p.value)
print(p.value + 2)
p.value = 10
print(p.y)
p.y = 12
print(p.y)
