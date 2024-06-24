s1={"python","java","perl"}
print(s1)
#convert list to set
s=set([12,13,14,150,15,12,12,15,100])
print(s)

#convert string to set
s=set("Abra ka dabra")
print(s)
#empty set
s=set()


s1={"python","java","perl"}
print(s)
#to add new value in the set
s1.add("OS")
s1.add("python")

s1.add("Python")
print(s1)
s1.add((12,13))
print(s1)
#s1.add([34,56])  #cannot add mutable values in set

s1.update({"ML","AI","database"})
print(s1)


