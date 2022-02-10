# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of Python course available on CourseGalaxy.com

class Fraction:
    def __init__(self,nr,dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:    
            self.nr *= -1
            self.dr *= -1

    def show(self):
        print(f'{self.nr}/{self.dr}')
       
f1 = Fraction(2,3)
f1.show()
f2 = Fraction(2,-3)
f2.show()
f3 = Fraction(-5,-6)
f3.show()
