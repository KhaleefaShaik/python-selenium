"""
Created on Feb 1, 2020
@author: Khaleefa Shaik
In this file will discuss about lambda expression, filters, map reduce datatypes in python
1. Lambda expression simply fies the code
2. filter will use to filter the list,tuple, set and directories using lambda expression
3. Map will use to do operation on all the elements of the given list,tuple, set and directories using lambda expression
4. Reduce will use to do operation on all the elements of the given list,tuple, set and directories using lambda expression
"""
from functools import reduce

l1 = [1, 2, 3, 4]
l2 = []


def m1():
    for i in l1:
        if i % 2 == 0:
            l2.append(i)
    print(l2)


m1()

x = lambda y: y % 2
print(x(20))

a = lambda x, y: x * y
print(a(5, 6))

a = lambda x, y: x if x * y > 10 else y
print(a(1, 100))

a = lambda k1: k1 + [1, 2]
print(list(a([10, 20])))

a = lambda i, j, k: i if i > (j and k) else j
print(a(1000, 200, 300))

"""filters
filter (expression, input)"""

print(list(filter(lambda x: x % 2 == 0, [10, 2, 3, 4, 1, 6, 7, 20])))

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 10]

l2 = list(filter(lambda x: x > 7, l1))
print(l2)

l2 = list(map(lambda x: x > 7, l1))
print(l2)

print(list(filter(lambda x: x == "ratan", ['ratan', 'durga', 'anu', 'khaleefa', 'ratan'])))
print(tuple(filter(lambda x: x == "ratan", ['ratan', 'durga', 'anu', 'khaleefa', 'ratan'])))
print(set(filter(lambda x: x == "ratan", ['ratan', 'durga', 'anu', 'khaleefa', 'ratan'])))

print(list(map(lambda x: x + " IT", ["Khaleefa", "Shaik", "Sha", "Vali"])))
print(list(map(lambda x: x + " IT " if x == "Vali" else x, ["Khaleefa", "Shaik", "Sha", "Vali"])))

l1 = [1, 2, 3, 4]
l2 = [10, 20, 30, 40]
print(list(l1 + l2))
print(l1 + l2)

print(tuple(map(lambda x, y: x + y, l1, l2)))
print(tuple(map(lambda x, y: x * y, l1, l2)))

str1 = "hi ratan sir how are you"
l1 = str1.split()
print(l1)
print(list(map(lambda x: len(x), l1)))
print(reduce(lambda x, y: x + y, l1))
print(reduce(lambda x, y: x + y, list(map(lambda x: len(x), l1))))
print(reduce(lambda x, y: x + y, range(1, 100)))
print(reduce(lambda x, y: x - y, range(1, 100)))
print(reduce(lambda x, y: x * y, range(1, 100)))
