# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:12:15 2021

@author: anilk
"""

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
                      
    
class B(A):
     def __init__(self,b1=0,**kwarg):
        print("B: ",kwarg) 
        super().__init__(**kwarg) #a1=12,a2=13,c1=31,c2=32
         #A.__init__(self,a1,a2)
        self.__b1=b1
       
     def __str__(self):
        return super().__str__()+f"B1: {self.__b1} "
    
class C(A):
    def __init__(self,c1=0,c2=0,**kwarg):
        print("C : ",kwarg)
        super().__init__(**kwarg)  #a1,a2
        #A.__init__(self,a1,a2)
        self.__c1=c1
        self.__c2=c2
        
    def __str__(self):
        return super().__str__()+f" C1: {self.__c1}, c2: {self.__c2}"
        
class D(C,B):
    def __init__(self,d1=0,d2=0,**kwarg):
        print("D : ",kwarg)
        #B.__init__(self,a1,a2,b1)
        #C.__init__(self,a1,a2,c1,c2)
        super().__init__(**kwarg)  #a1=12,a2=13,b1=21,c1=31,c2=32
        self.__d1=d1
        self.__d2=d2
    def __str__(self):
        return super().__str__()+f"D1 :{self.__d1}, D2: {self.__d2}"
        
ob=D(a1=12,a2=13,b1=21,b2=9,c1=31,c2=32,d1=41,d2=42)
print(ob)  
print(D.mro())   #method resolution order
 
    
    
    
    