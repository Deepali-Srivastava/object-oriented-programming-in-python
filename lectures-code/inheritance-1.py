# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of Python course available on CourseGalaxy.com

class Person:
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone

    def greet(self):
        print('Hello I am', self.name)

    def is_adult(self):
        if self.age > 18:
            return True
        else:
            return False
        
    def contact_details(self):
        print(self.address, self.phone)


class Employee(Person):
   pass

 
emp = Employee('Jack', 30, 'D4, XYZ Street, Delhi', '994477291')

print(emp.name)
print(emp.age)
print(emp.address)
print(emp.phone)

print(emp.greet())
print(emp.is_adult())
print(emp.contact_details())

print(isinstance(emp,Employee))  
print(isinstance(emp, Person))  

print(issubclass(Employee, Person))
print(issubclass(Person, object))
print(issubclass(str, object))
print(issubclass(int, object))
