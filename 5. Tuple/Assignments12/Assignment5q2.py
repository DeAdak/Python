s1 = input("Enter string: ")
check = input("Enter second string: ")
pos=s1.find(check)
while pos!=-1:
    print(f"{check}-{pos}")
    pos = s1.find(check,pos+1)
print(f"count={s1.count(check)}")
