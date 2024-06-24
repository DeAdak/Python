s1="apple"
s2=s1
s3="apple"
print(id(s1))
print(id(s2))
print(id(s3))
s3="pear"
if s1 is s2:
    print("found")
else:
    print("not found")
if s1 is s3:
    print("found")
else:
    print("not found")
