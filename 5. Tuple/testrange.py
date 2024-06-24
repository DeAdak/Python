lst=[12,34,67,89]
for i in range(len(lst)):   #0
    print(lst[i])

for a in lst:  #list,tuple,sets,dictionary,frozenset all these are iterable object
               # inside the class __iter__ , __next__
    print(a)

for i in range(10):  #generator functions
    print(i)
print(range(10))
