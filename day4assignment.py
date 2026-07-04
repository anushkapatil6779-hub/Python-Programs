
#area and circumference if circle
radius = float(input("Enter radius: "))
pi = 3.14

area = pi * radius * radius
circumference = 2 * pi * radius

print("Area of Circle =", area)
print("Circumference of Circle =", circumference)


#swap 2 numbers without 3rd variable
a=int(input("enter first number:"))
b=int(input("enter second number:"))

a,b=b,a

print("after swapping:")
print("a=",a)
print("b=",b)


#average of 5 numbers
n1=float(input("enter number 1:"))
n2=float(input("enter number 2:"))
n3=float(input("enter number 3:"))
n4=float(input("enter number 4:"))
n5=float(input("enter number 5:"))

average=(n1+n2+n3+n4+n5)/5
print("Average=",average)


#memory addressing using id()
a = 10
b = 3.14
c = "Hello"
d = True
e = [1, 2, 3]
f = (4, 5, 6)

print("int address =", id(a))
print("float address =", id(b))
print("string address =", id(c))
print("bool address =", id(d))
print("list address =", id(e))
print("tuple address =", id(f))

#bitwise operations on 2 hexadecimal numbers
a = int(input("Enter first hexadecimal number: "), 16)
b = int(input("Enter second hexadecimal number: "), 16)

print("AND =", hex(a & b))
print("OR =", hex(a | b))
print("XOR =", hex(a ^ b))
print("NOT a =", hex(~a))
print("NOT b =", hex(~b))
print("Left Shift a =", hex(a << 1))
print("Right Shift a =", hex(a >> 1))


#shopping bill
# Shopping Bill - 5 Products

print("===== SHOPPING BILL =====")

# Product 1
name1 = input("Enter product 1 name: ")
qty1  = int(input(f"Quantity of {name1}: "))
price1 = float(input(f"Price of {name1}: "))

# Product 2
name2 = input("Enter product 2 name: ")
qty2  = int(input(f"Quantity of {name2}: "))
price2 = float(input(f"Price of {name2}: "))

# Product 3
name3 = input("Enter product 3 name: ")
qty3  = int(input(f"Quantity of {name3}: "))
price3 = float(input(f"Price of {name3}: "))

# Product 4
name4 = input("Enter product 4 name: ")
qty4  = int(input(f"Quantity of {name4}: "))
price4 = float(input(f"Price of {name4}: "))

# Product 5
name5 = input("Enter product 5 name: ")
qty5  = int(input(f"Quantity of {name5}: "))
price5 = float(input(f"Price of {name5}: "))

# Calculations
total_quantity = qty1 + qty2 + qty3 + qty4 + qty5

amount1 = qty1 * price1
amount2 = qty2 * price2
amount3 = qty3 * price3
amount4 = qty4 * price4
amount5 = qty5 * price5

total_amount = amount1 + amount2 + amount3 + amount4 + amount5
average_price = total_amount / 5

# Bill Print
print("\n===== BILL RECEIPT =====")
print(f"{name1:15} x{qty1}  = Rs.{amount1}")
print(f"{name2:15} x{qty2}  = Rs.{amount2}")
print(f"{name3:15} x{qty3}  = Rs.{amount3}")
print(f"{name4:15} x{qty4}  = Rs.{amount4}")
print(f"{name5:15} x{qty5}  = Rs.{amount5}")
print("========================")
print(f"Total Quantity : {total_quantity}")
print(f"Total Amount   : Rs.{total_amount}")
print(f"Average Price  : Rs.{average_price}")
print("========================")

