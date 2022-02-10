# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of Python course available on CourseGalaxy.com

class Car:
   def start(self):
       print('Engine started')
   def move(self):
       print('Car is running')
   def stop(self):
       print('Brakes applied')
      
class Clock:
   def move(self):
       print('Tick Tick Tick')
   def stop(self):
       print('Clock needles stopped')


class Person:
    def move(self):
        print('Person walking')
      
    def stop(self):
        print('Taking rest')

    def talk(self):
        print('Hello')

car = Car()
clock = Clock()
person = Person()

def do_something(x):
   x.move()
   x.stop()

do_something(car)
do_something(clock)
do_something(person)
 
