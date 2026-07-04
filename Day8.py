
#list and their operations
marks=[90,98,90,85,96,75]
print(marks)
print(marks[2])
print(marks[-1])
print(marks[3:5]) #by using slicing
print(marks[::-1])
marks.reverse()
print(marks)

#replace an element
std=["y","x","j","a","t","q"]
std[1]="n"
print(std)


#replace an element
std=["y","x","j","a","t","q"]
std[4]="z"
print(std)


#add an element by using append function
std=["y","x","j","a","t","q"]
std.append("l")
print(std)


#add an element by using insert function
std=["y","x","j","a","t","q"]
std.insert(3,"v")
print(std)


#add an element by using extend function
std=["y","x","j","a","t","q"]
std2=["o","p"]
std.extend(std2)
print(std)


#remove an element by using remove and pop function
std=["y","x","j","a","t","q"]
std.pop()
print(std)

std.pop(1)
print(std)

std.remove("a")
print(std)

del std[0]
print(std)

std.clear()
print(std)

#in built functions of list
num=[9,8,7,4,5,6,7,8]
print(num.count(8))
print(num.index(5))
print(len(num))
print(min(num))
print(max(num))

#by using sort function
num=[9,8,7,4,5,6,7,8]
num.sort()
print(num)
num.sort(reverse=True)
print(num)

#by using sort function we perform character sorting
char=["a","b","z","v","x","f","j","l"]
char.sort()
print(char)
char.sort(reverse=True)
print(char)

#list concatnation
num=[9,8,7,4,5,6,7,8]
num2=[1,2,3]
print(num+num2)
rep=num2*3
print(rep)


#list comprasion
list=[i for i in range(1,101)]
print(list)

sq=[i*i for i in range(1,101)]
print(sq)


#nested list
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0])
print(matrix[0][0])
print(matrix[2][1])
print(matrix[2][0])




























































