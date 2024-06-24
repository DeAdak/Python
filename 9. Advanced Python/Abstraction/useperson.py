# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 21:07:09 2021

@author: anilk
"""

#from personclass import Person
from personservice import *    

choice=0
while choice!=8:
    print("1. add new person\n2. display by id\n3. display name\n4.modify mobile\n5.delete by id")
    print("6. display all\n7. sort by name\n8. exit")
    choice=int(input("enetr choice"))
    if choice==1:
        add_NewPerson()
    elif choice==2:
        pid=int(input("enter id for search"))
        p=searchById(pid)
        if p!=None:
            print(p)
        else:
            print(f"not found {pid}")
    elif choice==3:
        nm=input("enter name for search")
        p=searchByName(nm)
        if p!=None:
            for ob in p:
                print(ob)
        else:
            print(f"not found {pid}")
    elif choice==4:
        pid=int(input("enter id for mpdify"))
        nmob=input("enetr new mobile")
        status=modifyMobile(pid,nmob)
        if status:
            print("modification done")
        else:
            print("modification not done {pid}")
    elif choice==5:
         pid=int(input("enter id for delete"))
         status=deleteById(pid)
         if status:
             print("deletion done")
         else: 
             print(f"deletion not done for {pid}")
    elif choice==6:
        display_All()
    elif choice==7:
        sortByName()
    elif choice==8:
        print("thank you for visisting")
    else:
        print("wrong choice")