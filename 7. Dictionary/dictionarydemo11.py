courses={'DBDA':60,'DAI':80,'DTISS':120,'DIOT':60}
#to add a new key value pair
#if key is not there it will overwrite otherwise it will add new key value pair
courses['DAC']=240
print(courses)
#overwrite the value of DBDA key

courses['DBDA']=80
print(courses)

val=courses.get('DAC')
print(val)
print(courses)

val=courses.get('DAC123')
print(val)   #None
print(courses)
#it will return value if key exists otherwise it will return -1
val=courses.get('DAC123',-1)
print(val)   

#if key is not there then add key-value pair and return the value but
#if key exists then return the value of the existing key
val=courses.setdefault('DHPCSA',50)
print(courses)









