#mondaay.txt   --monday
#tuesday.txt ---- Tuseday

tuesday=[123,13,23,12]
monday=[123,145,23,12,15]
monset=set(monday)
tuesset=set(tuesday)
#present on both days
print(monset&tuesset)
#present on any one or both days
print(monset|tuesset)


s={123,234,345,234,456,345}

s1=frozenset(s)
s1.add(45)
