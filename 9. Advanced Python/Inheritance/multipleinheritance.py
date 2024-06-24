# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 16:45:37 2021

@author: anilk
"""

#multiple inheritance

class A:
    def __init__(self,a1=0,a2=0):
        self.__a1=a1
        self.__a2=a2
    
    def __str__(self):
        
        return f"A1: {self.__a1} , A2: {self.__a2}"
                      
    
class B:
     def __init__(self,b1=0):
         
        self.__b1=b1
       
     def __str__(self):
        return f"B1: {self.__b1} "
    
class C(A,B):
    def __init__(self,a1=0,a2=0,b1=0,c1=0,c2=0):
        #super().__init__(a1,a2,b1)  #error
        A.__init__(self,a1,a2)
        B.__init__(self,b1)
        self.__c1=c1
        self.__c2=c2
        
    def __str__(self):
        return A.__str__(self)+B.__str__(self)+f" C1: {self.__c1}, c2: {self.__c2}"
        

ob=C(12,13,21,31,32)
print(ob)    
    
    
    
    