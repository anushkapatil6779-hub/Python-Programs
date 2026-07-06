'''
#dictionary and its operations
student={"name":"a","age":25,"year":"fy"}
print(student["name"])
print(student["age"])
print(student["year"])

#by using update function
student.update({"phone_no":8552096779,"dept":"AIML","add":"kolhapur"})
print(student)

#search an element by using membership operators
print("age" in student)

#find keys of dictionary
print(student.keys())

#find values of dictionary
print(student.values())

#find items of dictionary
print(student.items())

#by using pop function remove an element
print(student.pop("year"))
print(student.popitem())
print(student.popitem())

print(student.clear())
print(student)

(del student["dept"])


#create a employee dictionary
emp={"name":"a","emp_id":101,"age":25,"dept":"aiml"}
print(emp)

#add an element in this dictionary
emp.update({"company":"platominds pvt.ltd kolhapur"})
print(emp)

#using loops access one by one element
for key in emp:
    print(key)

for values in emp.values():
    print(values)

for key,values in emp.items():
    print(key,values)
'''
#nested dictionary
info={101:{"name":"A","age":25,"dept":"cse"},102:{"name":"B","age":20,"dept":"aiml"}}
print(info)

print(info[101])
print(info[101]["name"])
print(info[101]["dept"])
print(info[101]["age"])


print(info[102])
print(info[102]["dept"])
print(info[102]["age"])
print(info[102]["name"])











































