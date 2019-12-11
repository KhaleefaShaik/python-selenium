'''
Created on Dec 5, 2019
@author: Khaleefa Shaik
'''

import keyword

print("Khaleefa Shaik")

# Keywords in python
print(keyword.kwlist)
'''
'False', 'None', 'True',
'and', 'as', 'assert',
'async', 'await', 'break',
'class', 'continue', 'def',
'del', 'elif', 'else',
'except', 'finally', 'for',
'from', 'global', 'if',
'import', 'in', 'is',
'lambda', 'nonlocal', 'not',
'or', 'pass', 'raise',
'return', 'try', 'while',
'with', 'yield'
'''

# Data types in python
'''
Python is a dynamic typed language, we need not to declare the data type explicitly
'''
name = 'Khaleefa'
department = "IT"
sal = 10000
age = 30
height = 6.1
isMale = True
print(type(name))
print(type(department))
print(type(sal))
print(type(age))
print(type(height))
print(type(isMale))

# variables reassigning in python
a = 100
print(a)

a = "Khaleefa Shaik"
print(a)

# swapping the variables in python
a,b = 200,"khaleefa"
print (a,b)
a,b=b,a
print (a,b)

# Deleting a variable in python
khaleefa = "name"
del khaleefa

# Prining the variables in python
'''
print(type(name))
print(type(department))
print(type(sal))
print(type(age))
print(type(height))
print(type(isMale))
'''
print("Employee Name is ", name)
print("Employee department is ", department)
print("Employee sal is ", sal)
print("Employee age is ", age)
print("Employee height is ", height)
print("Employee gender is male? ", isMale)

# print variable using %
print ("Employee Name is =%s Employee department is = %s  Employee sal is = %f" %(name,department,sal))
print("Employee age is = %d" %(age))
print("Employee height is = %d" %(height))
print("Employee gender is male? = %s" %(isMale))

#prining variable using {}
print ("Employee Name= {} Employee Age = {}" .format(name,age))

# taking an input from keyboard in python
# input(), always takes string inputs only

var1 = bool(input("Enter the first bloo variable:"))
var2 = bool(input("Enter the second bloo varaible"))
var3 = var1 + var2
print(var3)

var1 = float(input("Enter the first float variable:"))
var2 = float(input("Enter the second float varaible"))
var3 = var1 + var2
print(var3)

var1 = int(input("Enter the first int variable:"))
var2 = int(input("Enter the second int varaible"))
var3 = var1 + var2
print(var3)

var1 = int(input("Enter the first int variable:"))
var2 = float(input("Enter the second float varaible"))
var3 = var1 + var2
print(var3)

var1 = int(input("Enter the first int variable:"))
var2 = bool(input("Enter the second bool varaible"))
var3 = var1 + var2
print(var3)

'''var1 = float(input("Enter the first int variable:"))
var2 = str(input("Enter the second str varaible"))
var3 = var1 + var2
print(var3)'''