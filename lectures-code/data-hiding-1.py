# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of Python course available on CourseGalaxy.com

class Product:
    def __init__(self):
        self.data1 = 10
        self._data2 = 20
              
    def methodA(self):
        pass
            
    def _methodB(self):
        pass

p = Product()

print(p.data1)
p.methodA()
print(p._data2)
p._methodB()
