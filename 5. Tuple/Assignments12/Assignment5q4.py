city=[]
location=[]
print("City Names:")
ch='y'
while ch=='y':
    city.append(input("Enter city name:"))
    ch = input("add more cities?(y/n): ")
ch='y'
while ch=='y':
    location.append(input("Enter location:"))
    ch = input("add more locations?(y/n): ")

for a,b in zip(city,location):
    print(a,b)
