
#remove duplicate values
numbers=[10,20,50,20,100,25,60,10]
unique=[]
for i in numbers:
    if i not in unique:
        unique.append(i)
print(unique)    


#tuples data type and its operations
tup1=(20,30,40,55,68,25,45)
tup2=("a","l","o","h","m","c")
tup3=(3,"p",4,5,9,"a","f","w",100)
print(tup1[-2])
print(tup1[2:5])
print(tup3[2:5])


#
tup1=(20,30,40,55,68,25,45,40)
tup2=("a","l","o","h","m","c")
tup3=(3,"p",4,5,9,"a","f","w",100)
print(min(tup1))
print(min(tup2))

print(max(tup1))
print(max(tup2))

print(len(tup1))
print(len(tup2))
print(len(tup3))

print(sum(tup1))

print(tup1.count(40))

print(tup1[-2])
print(tup2[1])
print(tup3[-5])


#tuple packing and unpacking
student=("anushka",20,85)
name,age,marks=student
print(name)
print(age)
print(marks)
print(student)

x,y,z=15,80,75
print(z)

#swpping 2 elements
a=10
b=20
a,b = b,a 
print(a,b)


student=("anushka",20,85)
name,*b=student
print(name)
print(b)


tup=(20,30,40,55,68,25,45,2,5,7)
a,*b,c=tup
print(a)
print(b)
print(c)


tup=(20,30,40,55,68,25,45,2,5,7)
a,b,*c=tup
print(a)
print(b)
print(c)


char=("a","c","v","m","z","u")
a,*b,c=char
print(a)
print(b)
print(c)


#tuple concatnation 
tup1=(20,30,40,55,68,25,45,40)
tup2=("a","l","o","h","m","c")
print(tup1+tup2)
print(tup1.count(40))
print("o" in tup2)

search=int(input("enter a number"))
if search in tup1:
    print("number is present")
else:
    print("number is not present")
           
#tuple comparision
num=(i for i in range(1,101))
print(num)
print(tuple(num))


tup=((1,2,3),(6,8,9))
print(tup[0])
print(tup[1][2])
print(tup[1])






























    










      
