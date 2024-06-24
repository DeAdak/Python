# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 21:16:55 2021

@author: anilk
"""

from  personclass import Person
lst=[]
def add_NewPerson():
    pid=int(input("enetr id"))
    nm=input("enetr name")
    mobile=input("enetr mobile")
    p=Person(pid,nm,mobile)
    lst.append(p)
    
def display_All():
    for pob in lst:
        print(pob)
        
def searchById(pid):
    for pob in lst:
        if pob.get_pid()==pid:
            return pob
    else:
        return None
    
    
def searchByName(nm):
    plist=[]
    for pob in lst:
        if pob.get_pname()==nm:
            plist.append(pob)
    if len(plist)>0:
        return plist
    else:
        return None
    
def modifyMobile(pid,nmob):
    p=searchById(pid)
    if p!=None:
        print(f"Old mobile {p.get_mobile()} for pid : {p.get_pid()}")
        ch=input("do you want to modify")
        if ch=="y":
            p.set_mobile(nmob)
            return True
        else:
            return False
    else:
        return False
    
def deleteById(pid):
    p=searchById(pid)
    if p!=None:
        print(p)
        ch=input("do you want to delete")
        if ch=="y":
            lst.remove(p)
            return True
        else:
            return False
    else:
        return False
    
def sortByName():
    lst.sort(key=lambda x:x.get_pname()) 
    display_All()    
        
    
    
    
    
    
    