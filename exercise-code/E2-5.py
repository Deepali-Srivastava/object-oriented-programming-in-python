# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of Python course available on CourseGalaxy.com

class Book:
    def __init__(self,isbn, title,author,publisher,pages,price,copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies
   
    def display(self):
        print(self.title)
        print(f'ISBN : {self.isbn}')
        print(f'Price : {self._price}')
        print(f'Number of copies : {self.copies}')
        print('.' * 50)

    @property
    def price(self):
           return self._price

    @price.setter
    def price(self, new_price):
          if 10 <= new_price <= 500:
              self._price = new_price
          else:
               raise ValueError('Price cannot be less than 10 or more than 500')

book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 20,6)

book1.display()
book2.display()
book3.display()
book4.display()


