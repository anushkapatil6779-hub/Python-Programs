'''
#user defined functions in python
def greeting():
    print("welcome")
    print("to")
    print("class")
greeting()

#use of function to call name
def greeting():
    print("welcome")
    print("to")
    print("class")
    print("anushka")
greeting()

def greeting(name):
    print("welcome")
    print("to")
    print("class")
    print(name)
greeting("a")


#even_odd find
def even_odd(num):
    if num % 2 == 0:
        print("number is +ve")
    else:
        print("number is -ve")
even_odd(10)


#area of circle
def area(radius):
    pi=3.14
    circle_area=pi *(radius*radius)
    print("area of circle is :",circle_area)
area(3)

#area of rectangle
def rect(length,width):
    area=length*width
    print("area of rect is",area)
rect(8,2)

#sumission of two numbers
def add(num1,num2):
    add=num1+num2
    print("addition of two numbers is",add)
add(50,20)

#square of the number
def sq(num):
    square=num*num
    print("square is",square)
sq(8)


#return statement
def sq(num):
    return num*num
result=sq(3)
print(result)

#factorial number
def fact(n):
    if n==1:
        return 1
    return n*n-1
result=fact(5)
print(result)

#built_in functions innpython
list=[10,20,30]
print(len(list))
print(min(list))
print(max(list))


#by using string
str="anushka"
print(len(str))
print(min(str))
print(max(str))

#by providing lambda function adition
add=lambda a,b:a+b
print(add(5,8))

#by providing lambda function subtraction
sub=lambda a,b:a-b
print(sub(20,10))

#by providing lambda function multiplication
mul=lambda a,b:a*b
print(mul(20,10))
'''

























































    
