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
    def __init__(self, name, age, address, phone, salary, office_address, office_phone):
        super().__init__(name, age, address, phone)
        self.salary = salary
        self.office_address = office_address
        self.office_phone = office_phone

    def calculate_tax(self):
        if self.salary < 5000:
            return 0
        else:
            return self.salary * 0.05

    def contact_details(self):
        super().contact_details()
        print(self.office_address, self.office_phone)

emp = Employee('Jack', 30, 'D4, XYZ Street', '994477291', 8000, 'ABC Street', '384923993')
emp.contact_details()
