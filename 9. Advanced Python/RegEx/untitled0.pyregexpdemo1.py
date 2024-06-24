# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 15:38:23 2021

@author: anilk
"""

import re
s="Something is there somewhere"
m=re.match("s.*?e",s,re.I|re.M)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")
    

import re
s="something is there somewhere"
m=re.search("s.*?e",s)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")