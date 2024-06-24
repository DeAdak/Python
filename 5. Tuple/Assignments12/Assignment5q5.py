lst=[]
ch='y'
while ch=='y':
    lst.append(int(input("Enter number:")))
    ch = input("add more?(y/n): ")
list1=[]
len1=len(list1)
for index,value in enumerate(lst):
    while len1<= value:
        list1.append(-1)
        len1+=1
    list1[value]=index

print(list1)
    
