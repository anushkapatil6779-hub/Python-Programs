
f=open("demo.txt","w")
f.write("file content")
f.close()

#by using read+ function
f=open("demo.txt","r+")
f.write("abc")
data=f.read()
print(data)

f=open("demo.txt","r+")
f.write("abc")
f.seek(4)
data=f.read()
print(data)

#by using write+ method
f=open("demo.txt","w+")
f.write("anushka_patil")
data=f.read()
print(data)

#by using seek (seek ha fun ekada navin content write karnyasathi use kartata)
f=open("demo.txt","r+")
f.write("anushka_patil")
f.seek(3)
data=f.read()
print(data)

#second step
with open("demo.txt","r")as f:
    data=f.read()
    print(data)

#check data present or not in the entire file
word="learning"
with open("practice.txt","r")as f:
    data=f.read()
    if word in data:
        print(f"{word} is found")
    else:
        print(f"{word} is not found")

word="abc"
with open("practice.txt","r")as f:
    data=f.read()
    if word in data:
        print(f"{word} is found")
    else:
        print(f"{word} is not found")

word=input("enter a word")
with open("practice.txt","r")as f:
     data=f.read()
     if word in data:
         print(f"{word} is found")
     else:
         print(f"{word} is not found")


#counting lines 
data=True
line_no=1
word="learning"
with open("practice.txt","r")as f:
    while data:
        data=f.readline()
        if word in data:
            print(line_no)    
        line_no += 1   

#replace an element
with open("practice.txt","r")as f:
     data=f.read()
     
new_data=data.replace("c","python")
print(new_data)

with open("practice.txt","w")as f:
    f.write(new_data)
     

f=open("practice.txt","w+")     


#merge two files 
with open("demo.txt","r")as f1,open("practice.txt","r")as f2:
    data1=f1.read()
    data2=f2.read()

with open("merge.txt","w")as f3:
    f3.write(data1+"    "+data2)


#copy files
with open("merge.txt","r")as f1:
    data=f1.read()

with open("copy.txt","w")as f3:
    f3.write(data)
    

















































































     
        
        
