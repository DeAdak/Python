cities={'pune':['neem','mango','mohogani'],'mumbai':['coconut','supari','mangos']}
print(cities)
city='pune'
tree='nilgiri'
cities[city].append(tree)
print(cities)

nct=input("enter new city")
tr=[]
ans="y"
while ans=='y':
    t=input("enter tree")
    tr.append(t)
    ans=input("add more(y/n)")
cities[nct]=tr
print(cities)
