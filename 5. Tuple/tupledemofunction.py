def function1(a,b):
    a=a+10
    b=b+20
    return a,b

x=function1(23,45)
print(x)
print(type(x))
x,y=function1(23,45)
print(x,y)
print(type(x),type(y))

#zip,enumerate  tuple

lst=[12,13,14]
lst1=['aaa','bbbb','ccc','dddd']

##12    aaa
##13    bbb
##14    ccc

for a in lst:
    print(a)



                            # a,b=(12,'aaa')
for a,b in zip(lst,lst1):   #[(12,'aaa'),(13,'bbb'),(14,'ccc')]
    print(a,b,sep=",")




for index,value in enumerate(lst):   #[(0,12),(1,13),(2,14)]
    print(index,value)

#enumerate will start numbering from 10 onward
for index,value in enumerate(lst,10):   #[(10,12),(11,13),(12,14)]
    print(index,value)    

print([index for index,value in enumerate(list1) if value == 12])

lst.index(12)



