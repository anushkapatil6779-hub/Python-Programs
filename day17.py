
#by importing math function
import math
print(math.sqrt(25))
print(math.pi)
print(math.factorial(3))
print(math.pow(2,5))
print(math.ceil(12.7))
print(math.floor(12.7))

#by importing random function
import random as r
print(r.randint(1,100))
fruits=["banana","apple","grapes","mango"]
print(r.choice(fruits))

#select only random 5 values
for i in range(5):
    print(r.randint(1,100))
    

#by importing date-time function
import datetime
today=datetime.datetime.now()
print(today)
print(today.date())


#by using os function
import os
os.remove("python.txt")
print(os.getcwd())
print(os.listdir())

import mymodule
mymodule.say_hello("anu")

from mymodule import say_bye
say_bye("anushka")

from mymodule import say_hello
say_hello("anu")

from mymodule import std
print(std["age"])

from mymodule import std
print(std["name"])
