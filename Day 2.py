Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="10"
print(type(a))
<class 'str'>
b=3
print(a+b)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(a+b)
TypeError: can only concatenate str (not "int") to str
print(num+b)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(num+b)
NameError: name 'num' is not defined. Did you mean: 'sum'?
b=3
num=int(a)
b=3
print(num+b)
13
a=1.3
print(type(a))
<class 'float'>
b=2
sum=a+b
print(sum)
3.3
name=input("KPIT")
KPIT
name=input(a)
1.3
name=input("enter your name:")
enter your name:anushka patil
name=input()
kpit 
name=input("my college name is:",name)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    name=input("my college name is:",name)
TypeError: input expected at most 1 argument, got 2
name=input("my college name is:")
my college name is:k.p.patil institude of technology,mudal
a=int(input("enter your first number"))
enter your first number3
b=int(input("enter your second number"))
enter your second number2
sum=a+b
print(sum)
5


a=input("enter ur first number")
enter ur first number2
b=input("enter ur second number")
enter ur second number3
sum=a+b
print(sum)
23

x=input("first number")
first number2
y=input("second number")
second number3
sum = x+y
sum2 = int(x)+int(y)
print(sum)
23
print(sum2)
5

print("my name is:",name)
my name is: k.p.patil institude of technology,mudal
print(f"my name is {name} i am from kolhapur")
my name is k.p.patil institude of technology,mudal i am from kolhapur

science=int(input("enter your science marks:"))
enter your science marks:95
maths=int(input("enter your maths marks:"))
enter your maths marks:97
english=int(input("enter your english marks:"))
enter your english marks:98
obtained_marks=science+maths+english
print("obtained marks by students is:",obtained_marks)
obtained marks by students is: 290
#subtraction
goal=300
diff=goal-obtained_marks
print(f"student can achieve there target by achieving{diff}more marks")
student can achieve there target by achieving10more marks
#multiplication
book_price=150
no_books=34
total_amount=book_price*no_books
print("amount to pay:"total_amount)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(f"amount to pay:"total_amount)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("Amount to pay:"total_amount)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(amount to pay :total_amount)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("amount to pay:",total_amount)
amount to pay: 5100
>>> no_person=4
>>> country=total_amount/no_person
>>> print("amount to pay per person is:",total_amount)
amount to pay per person is: 5100
>>> print("amount to pay per person is:",country)
amount to pay per person is: 1275.0
>>> 
>>> #multiplication2
>>> book_price=200
>>> no_books=20
>>> total_amount=book_price*no_books
>>> print("amount to pay:",total_amount)
amount to pay: 4000
>>> no_person=5
>>> country=total_amount/no_person
>>> print("amount to pay per person is:",country)
amount to pay per person is: 800.0
>>> 
>>> #comparison
>>> a=10
>>> b=3
>>> print(a == b)
False
>>> print(a != b)
True
>>> greater_no=a>b
>>> print(greater_no)
True
>>> #comparison between character or string
>>> x="apple"
>>> y="banana"
>>> print(x>y)
False
>>> a="anushka"
>>> b="mrunal"
>>> print(a>b)
False
>>> a="anushka"
>>> b="mrunal"
>>> print(a<b)
True
