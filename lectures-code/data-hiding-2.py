# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of Python course available on CourseGalaxy.com

class Product:
    def __init__(self):
        self.data1 = 10
        self.__data2 = 20
              
    def methodA(self):
        pass
            
    def __methodB(self):
        pass

p = Product()
#print(p.__data2)
#p.__methodB()
print(p._Product__data2)
p._Product__methodB()
