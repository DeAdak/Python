s=" xxxyyyx     This   is string  xxx   "
s1=s.strip(" y")
print(s)
print(s1)
s1=s.lstrip(" y")
print(s)
print(s1)
s1=s.rstrip(" y")
print(s)
print(s1)
s="This is line\n"
s=s.rstrip("\n")


s1="xxxx1234:Rajan:w:34563:9-00am"
lst=s1.split(":")
print(lst)
acno=lst[0]
print(acno.lstrip("x"))

s2=",".join(lst)
print(s2)
