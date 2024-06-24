lst=[(10,'Ten'),(6,'six'),(1,'One'),(2,'Two'),(3,'three'),(5,'five')]
lst.sort()
print(lst)

lst.sort(key=lambda x: x[1])
print(lst)
