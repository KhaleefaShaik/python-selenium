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