#sets
A=[10,20,30,10,40,20,30,40,50,60,70,50]
print(A)

A={10,20,30,10,40,20,30,40,50,60,70,50}
print(A)


#using for loop access elements
p={10,20,30,40,50}
for i in p:
    print(i)
  
#using membership operator
p={10,20,30,40,50}
print(50 in p)
print(100 in p)


#create a multiple sets
set1={10,20,30,40,50}
set2={"a","b","c","d","e"}
set3={10,"s","d",34,"l",80,30,"c"}
#>>add only-one element
set1.add(60)
print(set1)

#>>add multiple elements
set1.update([70,80,90,100])
print(set1)

#>>remove specific element
set1.remove(10)
print(set1)

#>>remove random elements
set1.pop()
print(set1)

#>>clear all elements
set1.clear()
print(set1)


#aplly all functions to set2
set2.add("x")
print(set2)

set2.update(["s","d","m","r","k"])
print(set2)

set2.remove("a")
print(set2)

set2.pop()
print()

print(set2.pop())
print(set2.pop())

set2.clear()
print(set2)


#perform mathmatical operations(union |,intersection&,diff-,sym diff^
a={1,2,3,4,5,6,7}
b={6,7,8,9,0}
print(a|b) #print(a.union(b))
print(a&b) #print(a.intersection(b))
print(a-b) #print(a.difference(b))
print(b-a) 
print(a^b) #print(a.symmertric_difference(b))

#sub-set,super-set,joint-set,dis-joint set
a={1,2,3,4,5,6,7}
b={6,7,8,9,0}
c={1,2,3,4}
print(c.issubset(a))
print(a.issubset(c))
print(a.issuperset(c))
print(a.isdisjoint(c))


#frozenset
fs=frozenset([1,2,3,4,5])
print(type(fs))
print(fs)

















