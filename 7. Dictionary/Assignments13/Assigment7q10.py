##2. Given a dictionary of students and their favourite colours:
##people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
##1. Find out how many students are in the list
##2. Change Lisa’s favourite colour
##3. Remove 'Jenny' and her favourite colour
##4. Sort and print students and their favourite colours alphabetically by name


people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
choice=0
while choice<6:
    print("\n----------------------------------------")
    print("1. Find out how many students are in the list")
    print("2. Change Lisa’s favourite colour")
    print("3. Remove 'Jenny' and her favourite colour")
    print("4. Sort and print students and their favourite colours alphabetically by name")
    print("5. Display all details.")
    print("6. Exit.")
    choice = int(input("Enter your Choice: "))
    if choice==1:
        print("There are total",len(people),"students.")
    elif choice==2:
        color = input("Enter Lisa's new favourite colour: ")
        people['Lisa']=color
        print("Favourite Colour of Lisa updated.")
    elif choice==3:
        if 'Jenny' in people:
            people.pop('Jenny')
            print("Jenny has ben Removed.")
        else:
            print("Jenny not found.")
    elif choice==4:
        for name,color in sorted(people.items()):
            print(name,":",color)
    elif choice==5:
        print(people)
    else:
        print("-------------Thankyou-------------")
