# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:47:01 2021

@author: anilk
"""
import re
s1="Something is there somewhere"
m=re.search("S.*e",s1)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")


import re
s1="Something is there somewhere"
m=re.match(r"S.*e",s1)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")
    



