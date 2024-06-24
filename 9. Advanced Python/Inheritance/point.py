# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 14:50:17 2021

@author: anilk
"""

class Point:
    def __init__(self,x=0,y=0):
        self.__x=x
        self.__y=y
        
    def __str__(self):
        return f" x: {self.__x} , y: {self.__y}"
    
    def __add__(self,p):
        if isinstance(p, Point):
            x=self.__x+p.__x
            y=self.__y+p.__y
            
        else:
            x=self.__x+p
            y=self.__y+p
        return Point(x,y)
    
    def __radd__(self,p):
        x=self.__x+p
        y=self.__y+p
        return Point(x,y)

if __name__=="__main__":
    a=23
    b=45   
    p1=Point(a,b)
    p2=Point(23,34)
    print(p1)
    print(p2)
    p3=p1+p2    #p1.__add__(p2)
    print(p3)
    p4=p3+20
    p5=20+p3
    print(p4)
    print(p5)






