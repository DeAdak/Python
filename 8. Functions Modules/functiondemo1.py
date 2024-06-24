s=0
def f1(a,b,*t):
    print(a,b) # print value of a and b
    print(t)  #t is a tuple
    s=a+b
    for num in t:
        print(f"added {num}") 
        s=s+num
    return s

def f2(a,b,**kw):
    print(a,b)
    print(kw)
    s=a+b
    for k,v in kw.items():
        s=s+v
    return s

def f3(a,b):
    print(a,b)

f3(b=23,a=24)

    
s=f1(12,13,45,46,37,27,18,67)
print("addition: ",s)
s=f2(x=10,y=20,a=2,b=4)
print(
"addition : ",s)

