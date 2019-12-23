'''
Created on Dec 21, 2019
@author: Khaleefa Shaik
In this file will discuss about list datatypes in python

List is a datatype in python which stores the group of heterogeneous and homogeneous objects
List supports forward and backward indexing print(l1[-2]), print(l1[2:3:1]), print(l1[:]),print(l1[:2])
List preserves the insertion order
List allows the duplicates
List is mutable object where modifications are allowed
[] used to represent the list with , separated values

id(), is, is not - for memory comparision
== !=  for data comparision
in not in - to check the availability of an element


unpacking
list1 = [a,b,c]
e,f,g = list1

nested list, unpacking the nested list
for loops in list - in, range, nested listing using for loop
declaring a list using for loop l1 = [x for x in 10] l1 = [x for x in range [10,200]], l1 = [x for x in [10,100,20]]

Concatination
replicaiton
copy()
extend() add a list to another list
append() adds a elements to the list
insert(element), insert(element, index)

remove()
pop() - it will also removes an element from list, always it removes last element
pop(10) - index based elements removing from a list
del keyword - del l1[2], del l1[1:2] del l1 [:4:1]
clear()
sort(), sort(reverse=True)
Heterogeneous data sorting is not possible
index() - index(element), index(ele, range) - index("khaleefa", 2) - index("khaleefa", 2, 9)
reverse()
len
count()
max()
min()
'''

list1 = [1,2,4]
print(id(list1))

for x in list1:
    x = 3
    if x in list1:
        print("True")
    else:
        print("False")

list1 = []
list2 = []
if list1 is list2:
    print("List are same")
elif list1 > list2:
    print("List1 is > list 2")
elif list1 < list1:
    print("List1 is < list 2")
else:
    print("List are different")

x = 10
if x in list1:
    print(x)
else:
    print("element is not available in list")

#unpacking a list

list1 = [1,2,3,4]
a,b,c,d = list1
print(a)
print(d)

list1 = [[1,2],["A","B"]]

list2 = []
for x,y in list1:
    print(x,y)

empDetails = [[1,2,3],["Khaleefa","Shaik","Sha"]]
list1=[]
list2=[]
list3=[]

a, b = empDetails
print(type(a))
print(type(b))
eid1,eid2,ed3 = a
print(ed3)
for x,y,z in empDetails:
    list1.append(x)
    list2.append(y)
    list3.append(z)

print(list1)
print(list2)
print(list3)


list1 = [x for x in range (0,100,2)]
print(list1)

list2 = [x for x in range(1,100,2)]
print(list2)
print(list1+list2)
print(list1*2+list2*3)

list1 = [1,2,3]
list2 = list1.copy()
print(list2)

list2.extend(list1) # extends add the second list to first list
print(list2)

list3 = [5,6,7]
list3 = list1.copy() # copy replaces the list items
print(list3)

list3.append("Khaleefa") # append always adds an element at the end of the list
list3.insert(0,"Vali") # insert will add the element at the given index
list3.insert(5,"Sha")
print(list3)

#list3.remove(5)
print(list3)

list3.remove("Sha") # not possible to pass index
list3.pop(2) # removes the indexed element
list3.pop() # removes the last element
print(list3)

del list3[0]
print(list3)

list3.clear()
print(list3)

list3 = [x for x in range(100,20,-5)]
print(list3)
list3.sort(reverse=True)
list3.reverse()
#list3.sort(reverse=False)
print(list3)