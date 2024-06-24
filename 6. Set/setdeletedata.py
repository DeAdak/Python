s1={"python","java","perl"}
print(s1)
#pop,remove,discard
##print(s1.pop())
##print(s1)
##print(s1.pop())
##print(s1)
if "java1" in s1: 
    s1.remove("java1")  #if found then delete otherwise it will generate exception
    print(s1)
else:
    print("not exists")
s1.discard("java1")  #it will delete if found otherwise ignore

##{1,2,(12,13)}
##s1.add((12,13))
##
##{1,2,(12,13)}
##s1.update((12,13))
##
##{1,2,(12,13)}
###s1.add([12,13])#this is error
##
##{1,2,(12,13)}
##s1.update([12,13],[34,45])
##
##
##s1.update([12,12],[34,45])
##print("after update")
##print(s1)
##s1.add(tuple([12,13]))
        
