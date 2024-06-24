# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 20:07:36 2021

@author: anilk
"""
import re
lst=[]
ch='y'
while ch=='y':
    try:
        s=input("enetr data")
        m=re.search("^\d*$",s)
        if m==None:
            raise ValueError("do not enetr special characters or alphabates")
        else:
            lst.append(s)
            print("String added")
    except ValueError as e:
        print(e)
    ch=input("continue(y/n)")
print(lst)



s="test"
for ch in s:
    m=re.search("[aeiou]",ch)
    if m!=None:
        print("vowel")
    else:
        print("not vowel")
        
for ch in s:
    if ch in "aeiou":
       print("vowel")
    else:
        print("not vowel")

