'''
Created on Dec 21, 2019
@author: Khaleefa Shaik
In this file will discuss about strings in python
'''

# functions without arguments
def noArgs():
    ename, id = "Khaleefa", 500
    print(ename,id)

# functions with arguments
def withArgs(empName, eid):
    name, id = empName, eid
    return name, id

# Gloabs keyword

name = "Gloabal Name"
id = 799

def globalKeys():
    global name
    print(name)
    name = "Local Name"
    name1 = "Local var"
    def nonGlobalKeys():
        nonlocal name1
        print(name1)
    nonGlobalKeys()

# function with variable arguments
def reqArgs(*name):
    for name1 in name:
        print(name1)

# function with keyword args

def keyAgrs(name, id):
    print(name)
    print(id)

# functions without any return
def returnFun():
    x =100

#Function calling
noArgs()
print(withArgs("Vali", 600))
globalKeys()
print(name)
reqArgs(1,2,12,34,34,56,78,34)
keyAgrs(id=300,name="shavali")
print(returnFun())