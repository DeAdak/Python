# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 17:44:10 2021

@author: anilk
"""

lst=[]
from student import *
def add_NewStudent(ch):
    pid=int(input("enetr id"))
    nm=input("enetr name")
    mobile=input("enetr mobile")
    cnm=input("enetr course name")
    m1=float(input("enetr marks1"))
    m2=float(input("enetr marks1"))
    m3=float(input("enetr marks1"))
    if ch==1:
        paper=input("enetr paper topic")
        guide=input("enetr guide name")
        p=PhdStudent(pid,nm,mobile,cnm,m1,m2,m3,paper,guide)
        
    else:
        spsub=input("enetr specialsubject")
        p=GraduateStudent(pid,nm,mobile,cnm,m1,m2,m3,spsub)
    lst.append(p)
    
def display_All():
    for s in lst:
        print(s)
        
def search_By_Id(pid):
    for s in lst:
        if s.get_pid()==pid:
            return s
    else:
        return None
def  display_All_phd():
    for s in lst:
        if isinstance(s,PhdStudent):
            print(s)
    
def calculateMarks(pid):
    s=search_By_Id(pid)
    if s!=None :
        return s.calcPercet()   #dynamic polymorphism
    else:
        return None
    
        
        
        