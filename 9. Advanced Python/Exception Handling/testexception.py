# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 18:31:40 2021

@author: anilk
"""
d={"a":1,"b":2}
for i in range(3):
    try:
        num=int(input("enetr number"))
        num1=int(input("enetr number"))
        d1=num/num1
        print(d1)
        print(d["a"])
        print("your number is right")
        print(f"you enetred {num}")
        break
    except (KeyError,ValueError) as e:
        print("pls enter numeric data")
        print(e)
    except ZeroDivisionError as e:
        print("num2 cannot be zero")
        print(e)
    except:
        print("error occured")
    finally:
        print("in finally block")
else:
    print("your chances are done!! pls contact adminstrator")

