import re
list1=[]
ch='y'
while ch=='y':
    str1=input("Enter data(every element sep by comma) :")
    list1.append(str1)
    ch = input("want to add more?(y/n):")
    
print("Movie and year:-")
for val in list1:
    x = re.findall("[^0-9]2018,", val)
    if x:
        list2 = val.split(",")
        print(f"{list2[1]}, {list2[2]}")
        
print("Movie released in Pune:-")
for val in list1:
    x = re.findall("pune$", val,re.I)
    if x:
        list2 = val.split(",")
        print(list2[1])
