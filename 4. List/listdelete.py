lst=[12,34,56,40,50,38]
#to delete the data is pop, del, remove

lst.pop() #delete the data from the end
print("afetr pop()",lst)
lst.pop(4) #delete the data from 4 th position
print("afetr pop(4)",lst)
del(lst[3])
print("afetr del(lst[3])",lst)
if 34 in lst:
     lst.remove(34) # to delete by using value, it will delete the first occurance if founprint("afetr pop()",lst)d otherwise throw an exception
     print("removed")
else:
    print("not found")
print("afetr remove(34)",lst)

pos=lst.index(12)
lst[pos]=100
print(lst)

lst=[20,30,30,20,40,20,50,20]
#find number of occurances of 20
print("occurances",lst.count(20))
#delete all the values from the list
lst.clear()





