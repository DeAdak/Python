def f1(a,b):
    print("in f1")
    print(a,b)

def f2():
    print("in f2")

if __name__=="__main__":
    print("in module1",__name__)
    f1(12,13)
    f2()
    
