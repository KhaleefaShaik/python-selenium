"""
Created on Feb 4, 2020
@author: Khaleefa Shaik
In this file will discuss about class concept
1. constructors
2. instant methods
3. static methods
4. self keyword
5. __self__ this method will execute while printing the reference variable  of a class, it returns only
    string values
6. __del__ thiss method will execute when the reference variable is destroyed.
"""

class Employee():

    def __str__(self):
        return "This is the reference variable of this class"

    def __del__(self):
        print("The reference is destroyed")

    def __init__(self, eid, ename, esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def disp_emp_details(self):
        print("Employee id is ", self.eid)
        print("Employee name is ", self.ename)
        print("Employee salary is ", self.esal)

    @staticmethod
    def static_method():
        print("This is a static method")

    def instant_method(self):
        print("This is a instant method")

employee = Employee(1,"Employee_01", 100)
employee.disp_emp_details()
print(employee)
employee.instant_method()
Employee.static_method()
del employee