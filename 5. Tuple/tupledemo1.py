#tuples are mainly used to return multiple values from a function
a=(12,'aaa',45)
b=11,'aaa','bbbb',67   # packing
print(a,b)
print(len(a))
x,y,z=a    #unpacking of tuple

#list to tuple conversion can be done by using converter function
v=tuple([12,34,56,12,12,'xxx',34])
print("count 12",v.count(12))
print("position: ",v.index(12))

print(v)
#to create tuple of size 1
c=12,
print(type(c))
#v=tuple([12,23,45,67,tuple([56,78])])
print(v)

if 12 in v:
    pos=v.index(12)
    while True:
        print("position : ",pos)
        if 12 in v[pos+1:]:
            pos=v.index(12,pos+1)
        else:
            break
    
v=((12,10,10),(12,))

v[0].index(12)



