d1={'a':20,'b':30}
d2={'a':40,'c':50}
d1.update(d2)
print(d1)


v=d1.pop('a1',-1)
print(v)

print("after del")    
del(d1)
print(d1)

d1['x']=100
d1['y']=200
print(d1)
v=d1.popitem()
print(v)
