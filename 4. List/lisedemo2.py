lst=[] #empty list
num=int(input("enetr number"))
lst.append(num)   #increases length of the list by 1 and it will add the element at the end of list
lst.insert(0,45)  #insert function will add the data at 0th position
lst.extend([12,34,56])   #it adds multiple values at the end of the list
print(lst)
lst.append([10,30,50])
print(lst)
lst.insert(7,55)
print(lst)
#lst[9]=100  #thi is index error
lst.insert(9,100)
print(lst)
