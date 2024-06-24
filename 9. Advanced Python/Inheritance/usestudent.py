# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 17:39:59 2021

@author: anilk
"""
from Studentservice import *
print("1. Add new student\n 2. search By Id\n 3. Calculate marks\n4. display All \n5. display All phd student 6.exit")
choice=int(input("enter choice"))
if choice==1:
    print("1. Phd Student\n 2. Graduate Student")
    ch=int(input("enetr choice"))
    add_NewStudent(ch)
elif choice==2:
    pid=int(input("enetr pid"))
    s=search_By_Id(pid)
    if s!=None:
        print(s)
    else:
        print("not found")
        
elif choice==3:
     pid=int(input("enetr pid"))
     per=calculateMarks(pid)
     if per!=None:
         print(f"Pid : {pid} secured MArks: {per}")
     else:
         print("not found")
elif choice==4:
    display_All()
elif choice==5:
    display_All_phd()
elif choice==6:
    print("Thank you for visiting....")
else:
    print("wrong choice")