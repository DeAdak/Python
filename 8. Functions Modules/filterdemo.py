lst=[10,20,33,45,36,77]
lst2=[]
for num in lst:
    if num%3==0:
        lst2.append(num)
print(lst2)

lst2=[x for x in lst if x%3==0]
print(lst2)

def f1(x):
    return x%3==0

lst2=list(filter(lambda x:x %3==0 and x%7==0 ,lst))

lst2=list(filter(lambda x:x>50 ,lst ))

d={'a':2,'b':3,'c':5,'d':1}
for x in d.item():
    if x[1]>3:
        lst3.append(x)

lst3=list(filter(lambda x:x[1]>3,d.items()))  #(a,2)
print(lst3)












