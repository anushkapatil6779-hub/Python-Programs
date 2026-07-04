'''
a=3
b=2
print(a==b and a>b)
print(a>=b and a>b)
print(a==b or a>b)
print(not(a>=b and a>b))
print(not(a==b or a>b))



#and,or operaters operations
chem=int(input("enter your chemistry marks:"))
phy=int(input("enter your physics marks:"))
maths=int(input("enter your maths marks:"))
print(chem >= 45 and phy >=45 and maths>=45)


kaju_katli=int(input("KG of kaju_katli:"))
laddu=int(input("KG of laddu:"))
barfi=int(input("KG of barfi:"))
print(kaju_katli >= 5 or laddu >= 5 or barfi >= 5)
print(not(kaju_katli >= 5 or laddu >= 5 or barfi >= 5))


#assignment operators
#addition
a=5
sum=a+2
print(sum)
sub=a-2
print(sub)

#subtraction
a=5
a+=2
print(a)
a-=2
print(a)

#multiplication
a*=2
print(a)
a/=4
print(a)
a%=2
print(a)


a=0b1010
b=0b1100

op_1=a&b
print(op_1)
print(bin(op_1))

op_2=a/b
print(op_2)

op_3=a*b
print(op_3)
print(bin(op_3))

#q2)
a=0b1111
b=0b1100
op_1=a&b
print(op_1)
print(bin(op_1))

op_2=a/b
print(op_2)

op_3=a*b
print(op_3)
print(bin(op_3))

Class=["A","C","D","F","X","Z"]
result="A" in Class
print(result)
result="Q" in Class
print(result)

b="apple"
result="1" in b
print(result)
result="J" in b
print(result)

a=10
b=20
c=10
print(a==c)
print(a is c)
print(a is b)
print(id(a))
print(id(c))
print(id(b))
'''




