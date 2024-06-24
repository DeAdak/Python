# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 18:59:11 2021

@author: anilk
"""
class AgeError(Exception):
    def __init__(self,msg="error occured"):
        self.__msg=msg
    def __str__(self):
        return self.__msg


while True:
    try:
        age=int(input("enetr data"))   #15
        if age<18 or age>60:
            raise AgeError("age should be between 18 and 60")
        print(age)
        break
    except AgeError as e:
        print(e)
        


import re
try:
    nm=input("enetr data")
    m=re.search(r"^[A-Za-z0-9]*$",nm)
    if m==None:
        raise AgeError("special characters are not allowed")
    print(nm)
except AgeError as e:
    print(e)







