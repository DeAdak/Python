lst=[12,34,56,2,3,7,100]

lst.reverse()
print(lst) #reverse the list

lst.sort() #it works only on the list which has same type of data
print(lst) #this will print sorted list
lst.sort(reverse=True) #it works only on the list which has same type of data
print(lst) #this will print sorted list

lst=[12,34,56,2,3,7,100]
for num in sorted(lst):
    print(num)

print(lst)

#without changing original list it will revers the list
for num in reversed(lst):
    print(num)

print(lst)
