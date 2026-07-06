#q1)
import csv

f = open("product.csv", "w", newline="")
w = csv.writer(f)

w.writerow(["Name", "Price", "Rating"])
w.writerow(["Mobile",15000,4.5])
w.writerow(["Laptop",50000,4.8])
w.writerow(["Mouse",500,4.2])
w.writerow(["Keyboard",1200,4.3])
w.writerow(["Headphone",2000,4.6])

f.close()

print("Product CSV created")

#q3)
import csv

f = open("product.csv","r")
r = csv.reader(f)

for i in r:
    print(i)

f.close()

#q4)
import csv

name = input("Enter product name : ")

f = open("product.csv","r")
r = csv.reader(f)

next(r)

for i in r:
    if i[0].lower() == name.lower():
        print("Found :", i)

f.close()

#q5)
import csv

count = 0

f = open("product.csv","r")
r = csv.reader(f)

next(r)

for i in r:
    count += 1

print("Total products =", count)

f.close()

#q6)
import csv

lst = []

f = open("product.csv","r")
r = csv.reader(f)

next(r)

for i in r:
    lst.append(i)

print(lst)

f.close()


#q7)
import csv

price = input("Enter price : ")

f = open("product.csv","r")
r = csv.reader(f)

next(r)

for i in r:
    if i[1] == price:
        print(i)

f.close()

#q8)
import csv

rating = input("Enter rating : ")

f = open("product.csv","r")
r = csv.reader(f)

next(r)

for i in r:
    if i[2] == rating:
        print(i)

f.close()

#q10)
import csv

f = open("product.csv","r")
r = csv.reader(f)

next(r)

for i in r:
    print("Name =", i[0], "Price =", i[1])

f.close()


#q11)
import csv

f = open("product.csv","r")
r = csv.reader(f)

next(r)

max_price = 0

for i in r:
    if int(i[1]) > max_price:
        max_price = int(i[1])

print("Highest Price =", max_price)

f.close()

#q12)
import csv

f = open("product.csv","r")
r = csv.reader(f)

next(r)

prices = []

for i in r:
    prices.append(int(i[1]))

print("Lowest Price =", min(prices))

f.close()


































































