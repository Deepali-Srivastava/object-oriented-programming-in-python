
# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of Python course available on CourseGalaxy.com

class Account():
       rate = 5
       def some_method(self): 
          print(self.rate, Account.rate, id(self.rate), id(Account.rate))
          self.rate = 10
          print(self.rate, Account.rate, id(self.rate), id(Account.rate))
     
a1 = Account()
a2 = Account()
a1.some_method() 
