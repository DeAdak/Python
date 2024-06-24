#to check whether given number is prime
#7  --- divisible by 2 to 6 if yes then not prime if no then prime

##num=int(input("enter number"))
##flag=True
##for i in range(2,7):
##    if num % i ==0:
##        flag=False
##        break
##if flag:
##    print(f"the number is prime : {num}")
##else:
##    print(f"the number is not  prime : {num}")
##    

num=int(input("enter number"))
#flag=True
if num<2: #it is for num==1
    print(f"It is not a prime number {num}")
else:  #num 2 onward
    for i in range(2,num):  2,5
        if num % i ==0:  #39
            print(f"The number is not prime : {num}")
            #flag=False
            break
    else:
        print(f"the number is prime : {num}")
    
#if flag:
#    print(f"the number is prime : {num}")
#else:
#    print(f"the number is not  prime : {num}")







        
