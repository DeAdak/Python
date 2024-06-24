s1="js hj hjh jfhjkh kjhfdf This  is line"
pos=s1.find("This")
s2=s1[pos:]
print(s2)

name='Rajan'
marks=97
sub='Java'

#Rajan secured 97 marks in java
print(f"{name} secured {marks} marks in {sub}")
print( name+"secured"+str(marks)+" marks in"+sub)
print("{0} secured {1} marks in {2}".format(name,marks,sub))

s="This is apple, and you eat it"
if "apple" in s and "eat" in s:
    print("found")
else:
    print("not found")
s1="this tasty"
print(s1)
