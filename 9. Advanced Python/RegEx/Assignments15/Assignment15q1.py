import re
lst1=[]
dict1 = {'found':[],'not found':[]}
ch='y'
while ch=='y':
    str1 = input("Enter a line: ")
    lst1.append(str1)
    ch = input("Want to add more lines? (y/n): ")

mypat = re.compile("m$|mid$")    

for val in lst1:
    match = mypat.search(val)
    if match!=None:
        dict1['found'].append(val)
    else:
        dict1['not found'].append(val)

print(dict1)