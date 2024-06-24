import re

pat1 = input("Enter pattern 1: ")
pat2 = input("Enter pattern 2: ")

exp1 = re.compile(pat1)
exp2 = re.compile(pat2)

list1 = []
list2 = []
str1=""
while str1!='end':
    str1 = input("Enter a string: ")
    m1 = exp1.search(str1)
    m2 = exp2.search(str1)
    if m1!=None:
        list1.append(str1)
    elif m2!=None:
        list2.append(str1)
    elif str1!='end':
        print("Pattern not found")
        
print(f"List1: {list1}")
print(f"List2: {list2}")

