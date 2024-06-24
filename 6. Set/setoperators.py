s1={12,13,14,15}
s2={45,15,14}
print(s1,s2)
print(s1.difference(s2))
print(s1-s2) #only values which are in only s1 and not in s2
print(s1.difference_update(s2))
s1=s1-s2
print(s1) #only values which are in only s1 and not in s2
#issuperset
if s1.issuperset(s2): #s1>s2
    print("superset")
else:
    print("not superset")


if s1.issubset(s2):   #s1<s2
    print("subset")
else:
    print("not superset")

if s1.isdisjoint(s2):
    print("disjoint")
else:
    print("not disjoint")

if s1>s2:
    print("superset")
else:
    print("not superset")

#union of 2 sets
print(s1.union(s2)) #12,13,14,15,45
print(s1|s2)

#intersection
print(s1.intersection(s2)) #14,15
print(s1&s2)

#symmetric
print(s1.symmetric_difference(s2))
print(s1^s2)

#symmetric_difference_update
s1.symmetric_difference_update(s2)
print(s1)
s1=s1^s2
print(s1)

