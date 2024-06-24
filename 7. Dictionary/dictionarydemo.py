courses={'DBDA':60,'DAI':80,'DTISS':120,'DIOT':60}
print(courses)
print(courses['DBDA'])   #60
print(courses['DTISS'])
#print(courses['DAC'])
print('DAC' in courses)

#display alll values of a dicitonary
val=60
for k in reversed(courses.keys()):
    if courses[k]==val:
        print(k,"---->",courses[k])

    
for k in courses.values():
    print(k)

    
for k,v in courses.items():
    if v==val:
        print(k,"---->",v)
        
