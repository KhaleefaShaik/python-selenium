'''
Created on Dec 21, 2019
@author: Khaleefa Shaik
In this file will discuss about strings in python

String is one of the datatypes in python

supports both negative and positive indexing

String a immutable objects

len()
strip()
lsstrip()
rsstrip()

id() - to print the memory address, same strings points to same id
is , is not - operators will be used to string's memory comparision
in, not in - operators will be used to sub-string is present in the string or not

formatting a string in python
strings can be formatted in two ways'
using %s operation using format()
print("ename %s, eid %d" %(ename, eid))
print("ename{},eid{}" .format(ename,eid))
print("ename{1},eid{0}" .format(ename,eid))

concatenation and replications is python
print(s1 + s2)
print(s1*2 + s2*3)

relational operators
> < >= <= == !=

functions
upper(), lower(), join(), replace(), capitalize(), split(). enumerate(), count()
statswith(), endswith(), find(), index(), swapcase()
isalnum(), isalph(), isdigit()
islower(), isupper(), isspace()
sort()



'''

str1 = "Khaleef shaik sha vali"
str2 = "        k"
str3 = "      "
str4 = ""
print(type(str1))
print(id(str1))
print(id(str2))
print(id(str3))
print(id(str4))

print(str1[-1])
print(len(str1))
for c in range(0, len(str1)):
    print("Index of %s is %d" % (str1[c], c))

str1 = str1 + "Jee"
print(str1)

# print number of occurrences of a string
str1 = "Khaleefa Shaik Sha Vali"
count = 0
for s in str1:
    if s == 'k' or s == "K":
        count = count + 1
print("K or k reapeted %d times in the given string:" % count)

str1 = "Khaleefa Shaik Sha Vali"
if "Khaleefa12312" in str1:
    print("string present in the super string")
else:
    print("string not present in the super string")
if "Khaleeffa" is not str1:
    print("True")

str1 = "--------------Khaleefa Shaik Sha Vali---------------"
print(str1)
print(str1.lstrip('-'))
print(str1.rstrip('-'))
print(str1.strip(' '))
print(str1.upper())
print(str1.lower())
print(str1.isupper())
print(str1.islower())
print(str1.count('-'))
print(str1.index('V'))
print(str1.capitalize())
print(str1.join("Person"))
str2=['Khaleefa','Shaik','Sha','Vali']
str1='--'
str3="Khaleefa"
print(str1.join(str2))
print(str1.join(str3))
print(str3.join(str1))

str1 = "Khaleefa"
str2 = 'z'
print(str1.replace("lee","zee"))
print(str1.replace("e",'X',10)) # actual, expected, count (number of times to replace)

str1 = "KHALEEFA"
str2 = "khaleefa"
str3 = "KhaLeeFa"
str4 = "khaleefa shaik sha vali"
print("===============")
print(str1.capitalize())
print(str2.capitalize())
print(str3.capitalize())
print(str4.capitalize())

list1 = str4.split(' ')
list2 = []
for x in list1:
    list2.append(x.capitalize())

print(str(list2))

str1='a'
print(str1.capitalize())
str1="Khaleefa"
obj1 = enumerate(str1)
print(obj1)

for x in enumerate(str1):
    print(x)

print(list(enumerate(str1)))
print(list(enumerate(str1,100)))
print(str1.count("E"))
print(str1.count("e"))

str1 = "Khaleefa Shaik Sha Vali"

emp = {}
for x in str1:
    if x == " ":
        continue
    if x in emp:
        emp[x] = emp[x] + 1
    else:
        emp[x] = 1
print(emp)

str1 = "Khaleefa Shaik Sha Vali"
print(str1.startswith("K"))
print(str1.endswith("i"))
print(str1.endswith('k',9,14))
print(str1.startswith('S',15,20))

print(str1.find("Sha")) # return the position of the element
print(str1.index("Sha"))
#print(str1.index('z'))
print(str1.find("z"))
print(str1.swapcase())
str1="BCA123"
print("===============Last==========")
print(str1.isalnum())
print(str1.isalpha())
print(str1.isdigit())
print(str1.isspace())