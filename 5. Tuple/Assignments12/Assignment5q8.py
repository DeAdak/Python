def myFunc(e):
  return e[1]

list1=[]
ch='y'
while ch=='y':
    str1 = input("Enter string: ")
    list1.append(str1)
    list1.sort(key=myFunc)
    print(list1)
    ch=input("Add more?(y/n): ")
    
