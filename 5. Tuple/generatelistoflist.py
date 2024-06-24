lst=[]
#12,55,13,15,78,34,56,88
##  0  1    2  3  4  5
##[[],[12],[],[],[],[]]

##1-10   0
##11-20  1
##21-30  2
##31-40  3

ans='y'
while ans=='y':
    num=int(input("enetr number"))
    pos=num//10
    if num%10==0:
        pos=pos-1
             #24-10   14//10 1
    #pos=abs(num-10)//10    #5
    if pos > len(lst):
                        
        for i in range(pos-len(lst)+1):
            lst.append([])
    lst[pos].append(num)
    print(lst)
    ans=input("continue (y/n)")
print(lst)
