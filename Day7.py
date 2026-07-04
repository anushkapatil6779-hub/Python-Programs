
# check types of single line
str="name"
print(type(str))
a="123"
print(type(a))
b=123
print(type(b))

#multiple lines show in one line
a='welcome to class "python"'
print(a)

b="welcome to class 'python'"
print(b)

#by using unwanted space
str="   Hellow world"
print(str)
print(str.strip())


def space(name):
    new_name.strip()
    print(new_name)
space(input("anushka"))


#by using split function
str="python is a programming language"
print(str.split())


str="python-is-a-programming-language"
print(str.split("-is-a-"))


str="K#P#Patil#institude#of#technology#mudal"
print(str.split("#Patil#institude#of"))

#indexing 
a="hellow world"
print(a[3])
print(a[6])
print(a[-1])
print(a[-6])

#by using index access specific elements(slicing method)
a="hellow world"

print(a[7:])
print(a[:6])
print(a[0::3])
print(a[-6:-1])
print(a[::-1])

#string concatnation
s1="anushka"
s2="patil"
full_name=s1+s2
print(full_name)

#with space
s1="anushka"
s2="patil"
full_name=s1+" "+s2
print(full_name)


#repeatdly print 
s1="anushka"
s2="patil"
full_name=(s1*3)
print(full_name)


str="python"
new=str[0:2]*2
print(new)
print(new+str)

#string methods
str="python programming language"
print(str.upper())
print(str.lower())
print(str.count("g"))
print(str.find("m"))
print(str.title())


















