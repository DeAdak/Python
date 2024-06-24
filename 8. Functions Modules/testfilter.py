dict1 = {'cat': [10,25,42], 'bat': [20,25], 'mat': [30,10]}
lst4=list(filter(lambda x:x%5==0  ,dict1['cat']))
print(lst4)


lst=[10,20,30,40]

lst11=list(map(lambda x:x*x, lst))
print(lst11)

import functools
s=functools.reduce(lambda x,y:x+y,lst)

s=functools.reduce(lambda x,y:x if x<y else y,lst)



