'''
Created on Dec 12, 2019
@author: Khaleefa Shaik
In this file will discuss about flow controls in python
'''

# Conditional statements in python
number = 5031
if number % 2 == False:
    print("When %d is divided by 2 remainder is %d" %(number, False))
else:
    print("When %d is divided by 2 remainder is %d" %(number,True))

print("============ Second Example==============")
name = "Khaleefa Shaik Sha Vali"
name = name.split(" ")

if name[0]=="Khaleefa":
    print ("The person's first name is %s" %name[0])

print("============Example Three================")

browser = input("Please enter the required browser")
if browser == 'gc' or "GC" or "chrome" or "CHROME":
    print("The user has selected %s browser..!" % browser)
elif browser == 'ff' or "FF" or "firefox" or "FIREFOX":
    print("The user has selected %s browser..!" % browser)
elif browser == 'IE' or "ie" or "ineternetexplorer" or "INTERNETEXPLORER":
    print("The user has selected %s browser..!" % browser)
else:
    print("The user has selected %s browser..!" % browser)

# Iterations(Loops) in python
print("=============Example Four============")
for x in range(200):
    if x > 100:
        print("The number is %d" % x)
else:
    print("For loop iteration is completed")
for x in range (1,100):
    if x < 50:
        continue
    print("The number is %d" % x)
    if x == 60:
        break

for x in range (100, 200, 2):
    print(x)

for x in range (100, 50, -5):
    print(x)