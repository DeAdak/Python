# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 18:54:16 2021

@author: anilk
"""
object 


class Person:
    location="Aundh"
    #constructor-- default and parametrized constructor
    def __init__(self,pid=0,nm="",mob=""):
        print("in init of person")
        self.__pid=pid
        self.__pname=nm
        self.__mobile= mob      #private membres are accessible only within class
        #self._email="ldsfljdl"   #protected accessible to children and within class
        #self.data=34      #public members ---are accessible outside the class
     
    @staticmethod  
    def mystaticfunction(loc="Aundh"):
        Person.location=loc
        print(Person.location)
        
    def mym1(self):
        print("in mym1 method")
    
    #setter are used to modify value of one of the members
    def set_pid(self,pid):
        self.__pid=pid
        
    def set_pname(self,nm):
        self.__pname=nm
        
    def set_mobile(self,m):
        self.__mobile=m
    
    #is used to retrieve values of one of the members
    def get_pname(self):
        return self.__pname
    
    def get_pid(self):
        return self.__pid
    
    def get_mobile(self):
        return self.__mobile
    
    def __str__(self):
        print("in str of person")
        return f"PId : {self.__pid}, Name : {self.__pname}, mobile : {self.__mobile} location: {Person.location}"

if __name__=="__main__":        
    i=23
    p1=Person(12,"Rajan","1111")
    p2=Person(13,"Revati","2222")
    print(p1)
    print(p1.location)
    print(p2)
    print(p2.location)
    print(Person.location)
    Person.mystaticfunction("Baner")
    print(p1.location)
    print(p1.mym1())
    print(p1.get_mobile())
    print(p2.get_mobile())



