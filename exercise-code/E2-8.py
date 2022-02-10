# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of Python course available on CourseGalaxy.com

class Product():
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self.discount = discount
        
    @property
    def selling_price(self):
        return self.marked_price - 0.01 * self.discount * self.marked_price
    
    def display(self):
        print(self.id,  self.marked_price,  self.discount)
    
p1 = Product('A234', 100, 5)
p2 = Product('X879', 400, 6)
p3 = Product('B987', 990, 4)
p4 = Product('H456', 800, 6)

print(p1.id, p1.selling_price)
print(p2.id, p2.selling_price)
print(p3.id, p3.selling_price)
print(p4.id, p4.selling_price)
