import math
print(math.sqrt(4))
print(math.pi)

#string is internally treated as list of character
s1="This is cat, and cat is cute, where is your cat"
for ch in s1:
    print(ch)
#to find length of the string
print("length",len(s1))

print(s1[5:14])#it will print 5 to 13 characters
print(s1[:14])  #it will print 0 to 13 characters
print(s1[5:])  #it will print 5 till end characters
print(s1[:])  #it will print entire string
print(s1[5:30:2])  #it will print 5,7,9,11,.....,29
print(s1[::-1]) #it will reverse the string
print(s1[::2])
print(s1[-1])

