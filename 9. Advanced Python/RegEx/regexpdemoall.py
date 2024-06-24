# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 15:46:35 2021

@author: anilk
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 15:38:23 2021

@author: anilk
"""
import re
myreg=re.compile("s.*?e",re.I)

s="Something is there somewhere"
lst=myreg.findall(s)
#return list of strings
if lst!=None:
    print(lst)
else:
    print("not found")
    
import re
s="Something is there somewhere"
#return list of match objects
mlst=myreg.finditer(s)
if mlst!=None:
    for m in mlst:
        print(m.group())
        print(m.span())
else:
    print("not found")    
    

s="Something is there somewhere"
lst=re.findall("s.*?e",s,re.I|re.M)
#return list of strings
if lst!=None:
    print(lst)
else:
    print("not found")
    

import re
s="Something is there somewhere"
#return list of match objects
mlst=re.finditer("s.*?e",s)
if mlst!=None:
    for m in mlst:
        print(m.group())
        print(m.span())
else:
    print("not found")
    
    
 
s="something is there somewhere"
#return list of match objects
s1=re.sub("s.*?e","any",s,count=1,flags=re.I)
if s1!=None:
    print(s1)
else:
    print("not found")   
    
    
    
    
    