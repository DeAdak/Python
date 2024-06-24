#if the module is other folder
##import sys
##sys.path.append(r"c:\mydata")

#if it is in another package
##import mypackage1.module1
##
##
##print("in usemodule",__name__)
##module1.f1(10,20)
##module1.f2()
##print("in usemodule")


##import module1 as m
##
##
##print("in usemodule",__name__)
##m.f1(10,20)
##m.f2()
##print("in usemodule")


#from module1 import f1,f2
from module1 import *

print("in usemodule",__name__)
f1(10,20)
f2()
print("in usemodule")
