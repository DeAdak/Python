
def checkprime(num):
    if num<2: #it is for num==1
        return False
    else:  #num 2 onward
        for i in range(2,num):  #2,5
            if num % i ==0:  #39
                return False
                #flag=False
        else:
            return True


num=int(input("enter number"))
status=checkprime(num)
if status: # (status==True)
    print(num*2)
    print(f"The number is prime : {num}")
else:
    print(num*3)
    print(f"the number is not prime : {num}")


        
