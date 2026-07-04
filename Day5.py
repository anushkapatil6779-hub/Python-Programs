'''
pi=3.14
radius=float(input("enter radius"))
if radius >= 0:
    area=pi*(radius*radius)
    print(area)
else:
    print("Enter valid radius")

#age
age=int(input("enter your age"))
if age>=18:
    print("person is eligible for voting")
else:
    print("person is not eligible for voting")



#nested if
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))

if a>b and a>c:
    print(f" {a} is greater")
elif b>a and b>c:
    print(f" {b} is greater")
else:
    print(f" {c} is greater")

#looping statements
name=input("enter your name:")
x=0
while x <= 10:
    print(name)
    
#while loop 
number=int(input("enter your number"))
x=0
while x<=10:
    print(x)
    x += 1
    print("out of loop")


number=int(input("enter your number"))
y=1
while y <= 11:
    print(number*y)
    y += 1


#for loop
for i in range (1,11):
    print(i)
    

#by using step value
for i in range (1,11,2):
    print(i)
    

m=int(input("enter first number"))
n=int(input("enter second number"))
for i in range (m,n,-1):
    print(i)
    print(m)
    m -= 1


for i in range(1,101):
    if i % 5 == 0:
        print(i)

number=int(input("enter a number"))
for i in range(1,101):
    if i == 0:
        print(i)

#continue statement
for i in range (1,11):
    if i == 3:
        continue
    print(i)
    
for i in range (1,11):
    if i == 5:
        break
    print(i)


#nested loop
n=5
for i in range(n):
    print("*")

n=5
for i in range(n):
    print("*",end =" ")
 
n=5
for i in range(n):
    for j in range(n):
        print("*",end =" ")
    print()

n=5
for i in range(n):
    for j in range(i+1):
        print("*",end =" ")
    print()
'''
n=5
for i in range(n):
    for j in range(i +1):
        print("*",end =" ")
    print()


           
           































        


               


        

        
        
