#string is immutable
#list is mutable object
lst=[10,20,30]
lst1=lst
lst.append(100)
print(lst)
print(lst1)
lst3=lst.copy()
lst.append(200)
print(id(lst1))
print(id(lst))
print(id(lst3))
print(lst)
print(lst1)
print(lst3)
