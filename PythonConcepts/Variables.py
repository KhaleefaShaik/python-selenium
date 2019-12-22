'''
Created on Dec 14, 2019
@author: Khaleefa Shaik
In this file will discuss about variables in python
Global variables
Local variables
UnbondError A local variable can't be declare same as global after using the global variable
'''

a = 100
b = 200


def fun1(x, y):  # Local variable
    return x + y


def fun2():
    a = 200  # local variable
    b = 600  # local variable
    return a + b


def fun3():
    a = 100
    b = 10
    print(a + b)
    print(globals()['a'] + globals()['b'])


def fun4():
    global a
    global b
    print(a + b)


def fun5():
    c = a + b
    print(c)


""" a = 100
    b = 20
    print(a+b)"""

print(fun1(a, b))
print(fun2())
fun3()
fun4()
fun5()

# number system in python
# binary number system - Always starts with 0B 0r 0b will contains only 1, 0
a = 0B101010
print(a)
b = 0b111110000111001
print(b)

# octa number system - Always starts with 0o 0O will contains 0 - 7
a = 0O1237121236
print(a)
b = 0o1232342434572341123
print(b)

# decimal number system - Direct values
a = 10
print(a)

# hexa decimals - 0X 0r 0x 0-9 and a-f
a = 0Xabcd1231312339223482937
print(a)

print("==========saperator============")
print("a", "b", "c", "d", sep='1')
print("a", "e", "i", "o", "w", sep=" is a owel, ")

# function to find ascii value
print(ord('A'))
print(ord('a'))
print(ord("Z"))
print(bin(200))
print(hex(300))
print(oct(400))

# %d for int, %s for string %g for float will print upto 6 digits, %f for float will print up-to 17 digits
num = 1902839.123123
print("%g is a floating number" % num)
num = 19028391231231.12312312312312312
print("%f is a floating number" % num)

# global and local variable

a = "Khaleefa"

def pfun():
    global a
    a = 'Shaik'
    b = a

    def cfun():
        nonlocal b
        b = 'Sha'
        print(b)
    cfun()


pfun()
print(a)
print(globals()['a'])