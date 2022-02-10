# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of Python course available on CourseGalaxy.com

class Book():
       x = 5
       def __init__(self):
            self.x = 100
       def display(self):
           print(self.x)
           print(Book.x)

b = Book()
b.display()

print(Book.x)
print(b.x)
 
