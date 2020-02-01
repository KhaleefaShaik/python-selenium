"""
Created on Dec 26, 2019
@author: Khaleefa Shaik
In this file will discuss about tuple datatypes in python

tuple and list are similar data types in python, the only difference is
tuple is immutable object means modifications and manipulications are not allowed
tuple preserve
the inserion order, allows the duplication, returns the data bases on index
1.immutable
2. Basic example
3. indexing, unpacking, nested tuple
4. print data using for loop
5. declaring a tuple using for loop
6. id, is, is not, == , != , in, not in
7. concatination replication
9. conversion process
10. count index len
11. sorting and sorted(), sort()

"""

# Basic example and immutability of a tuple

t1 = (1,2,32,-1,"Raju")
print(t1)
print(id(t1))

t2=("rani",) # if only element is there in tuple have to separe with comma
print(type(t2))

t1 = t1 + t2
print(id(t1))
print(t1)

l1 = [1,2,32,-1,"Raju"]
print(l1)
print(id(l1))

l2=["rani"] # if only element is there in tuple have to separe with comma
print(type(l2))

l1 = l1 + l2
print(id(l1))
print(l1)


# 3. indexing, unpacking, nested tuple

t1 = tuple(x for x in range(100))
print(t1)
print(t1[-20])
print(t1[1:20:2])

l1 = t1[1:20:2]
print("New unpacted list is %s" % str(l1))


t1 = ((1,2,3),("A","B","C"),(True,False,False))
for x in t1:
    print(x)
t2 = []
t3 = []
t4 = []
for x,y,z in t1:
    t2.append(x)
    t3.append(y)
    t4.append(z)

print(tuple(t2))
print(tuple(t3))
print(tuple(t4))


# 4. print data using for loop

t1 = tuple(x for x in range (101))

for x in t1:
    if(x % 2 == 0):
        print("The element %d in the tuple is a even number" % x)
    else:
        print("The element %d in the tuple is a odd number" % x)


# 6. id, is, is not, == , != , in, not in
t1 = tuple()
t2 = tuple()
t3 = tuple()
print(id(t1))
print(id(t2))
print(id(t3))

t1 = (1,2,3)
t2 = (1,2,3,4)
t3 = (1,2,3)
print(id(t1))
print(id(t2))
print(id(t3))

print(t1 is t2)
print(t1 == t2)

print(4 in t3 )