ch='y'
list1=[]
len1=len(list1)
while ch=='y':
    num=int(input("Enter number: "))
    pos=num%10
    while len1<=pos:
        list1.append([])
        len1+=1
    list1[pos].append(num)
    ch = input("Add more numbers?(y/n):")
print(list1)
