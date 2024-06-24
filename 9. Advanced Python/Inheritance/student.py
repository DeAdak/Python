# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 16:04:45 2021

@author: anilk
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 18:54:16 2021

@author: anilk
"""
object 


class Person:
   
    #constructor-- default and parametrized constructor
    def __init__(self,pid=0,nm="",mob=""):
        print("in init of person")
        self.__pid=pid
        self.__pname=nm
        self.__mobile= mob      #private membres are accessible only within class
        #self._email="ldsfljdl"   #protected accessible to children and within class
        #self.data=34      #public members ---are accessible outside the class
     
    #setter are used to modify value of one of the members
    def set_pid(self,pid):
        self.__pid=pid
        self.__p1=23
        
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
        return f"PId : {self.__pid}, Name : {self.__pname}, mobile : {self.__mobile} "
from abc import ABC,abstractmethod
class Student(Person,ABC):
    def __init__(self,pid=0,nm="",mob="",cname="",m1=0,m2=0,m3=0):
        #Person.__init__(self,pid,nm,mob)
        super().__init__(pid,nm,mob)
        self.__course=cname
        self._m1=m1
        self._m2=m2
        self._m3=m3
        
    @abstractmethod    
    def calcPercet(self):
        pass
    
    def __str__(self):
         return super().__str__()+f"course : {self.__course} , M1: {self._m1}, M2 : {self._m2}, M3: {self._m3}"
     
class PhdStudent(Student):
    def __init__(self,pid=0,nm="",mob="",cname="",m1=0,m2=0,m3=0,paper="",gname=""):
      super().__init__(pid,nm,mob,cname,m1,m2,m3)
      self.__paper=paper
      self.__gname=gname
    def __str__(self):
        return super().__str__()+f" Paper: {self.__paper}, Guide : {self.__gname} "
    
    def calcPercet(self):
        return self._m1+self._m2+self._m3/100
    
    
class GraduateStudent(Student):
    def __init__(self,pid=0,nm="",mob="",cname="",m1=0,m2=0,m3=0,spsub=""):
      super().__init__(pid,nm,mob,cname,m1,m2,m3)
      self.__spsub=spsub
    def calcPercet(self):
        return self._m1+self._m2+self._m3+50/100 
    def __str__(self):
        return super().__str__()+f" Sp. subject : {self.__spsub} "
     
if __name__=="__main__":        
    i=23
    p1=Person(12,"Rajan","1111")
    p2=Person(13,"Revati","2222")
    print(p1)
    print(p2)
    
    s=Student(111,'rajat',"33333","DBDA",99,98,97)
    print(s)
    s=PhdStudent(111,'rajat',"33333","DBDA",99,98,97,"xxxxxx","Rajan")
    print(s)
    print(s.calcPercet())
    s=GraduateStudent(111,'rajat',"33333","DBDA",99,98,97,"Computer")
    print(s)
    print(s.calcPercet())

