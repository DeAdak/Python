#find addition of digits of a number

#345   3+4+5
#3456  3+4+5+6

##num=int(input("enetr number"))
##s=0
##n1=num
##while num!=0:
##    digit=num%10
##    s=s+digit
##    num=num//10  #345
##print(f"Sum of digits of {n1} : {s}")

#optional parameters 
def addition(a=3,b=5):
    a=a+10
    b=b+20
    return a+b

def sumdigits(num=202):
    s=0
    while num!=0:
        digit=num%10
        s=s+digit
        num=num//10
    return s

print(addition(2))
print(addition(3,7))
num=int(input("enter number"))
s=sumdigits(num)
print(f"sum of {num} : {s}")
    
s=sumdigits()
print(f"sum of {num} : {s}")
    
    
