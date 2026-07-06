#text file's operations and file  handling
f=open("note.txt","r")
data=f.read()
print(data)
f.close()


#giving range to access data
f=open("note.txt","r")
data=f.read(5)
print(data)
f.close()

#accessing single line 
f=open("note.txt","r")
data=f.readline()
print(data)
f.close


#access multiple lines
f=open("note.txt","r")
data=f.readline()
print(data)
data1=f.readline()
print(data1)
f.close()


#access all text format to list format
f=open("note.txt","r")
data=f.readlines()
print(data)
f.close


#write function
f=open("note.txt","w")
data=f.write("this line will add to your file")
print(data)
f.close()

#append function
f=open("note.txt","a")
data=f.write("\n appends data")
print(data)
f.close()
