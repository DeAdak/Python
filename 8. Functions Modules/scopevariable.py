def f1():
    #global x
    x=12
    print(x)
    def f2():
        #global x
        #nonlocal x
        x=23
        print(x)
    f2()    
    print(x)
    

x=100   #global
print(x)  #100
f1()
print(x)  #100 
