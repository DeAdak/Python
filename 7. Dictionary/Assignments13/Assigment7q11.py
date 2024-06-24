##3. Write a menu driven program to practice Dictionary functions.
##Write a program to accept name of a person and their vehicle and store
##it in a dictionary.
##Ask user if they want to continue to accept multiple values.

vehicle_dict={'Nishant':'Farari','Virat':'Audi'}

def delete_entry(name):
    val = vehicle_dict.get(name)
    if val is not None:
        print(f"Name: {name}\tVehicle: {val}")
        ch=input("Do you want to delete?(y/n):")
        if ch=='y':
            vehicle_dict.pop(name)
            return True
        else:
            return False
    else:
        print("Name not found")
        return False

def modify_entry(name):
    val = vehicle_dict.get(name)
    if val is not None:
        print(f"Name: {name}\tVehicle: {val}")
        ch=input("Do you want to modify?(y/n):")
        if ch=='y':
            val2=input("Enter new vehicle:")
            vehicle_dict.update({name:val})
            return True
        else:
            return False
    else:
        print("Name not found")
        return False

choice=0
while choice<8:
    print("\n--------------MENU-------------")
    print("1. Add new person name and a vehicle name.")
    print("2. Delete a person name and vehicle name from the dictionary.")
    print("3. Modify vehicle name for the person.")
    print("4. Search vehicle for the given person’s name.")
    print("5. Search list of people, who have given a vehicle.")
    print("6. Display all person names.")
    print("7. Display all vehicle names.")
    print("8. Exit.")
    choice=int(input("Enter your choice:"))
    if choice==1:
        name=input("Enter name:")
        vehicle=input("Enter vehicle name:")
        vehicle_dict.update({name:vehicle})

    elif choice==2:
        name=input("Enter name:")
        if delete_entry(name):
            print("Deleted successfully!!!")
        else:
            print("Not deleted")

    elif choice==3:
        name=input("Enter name:")
        if modify_entry(name):
            print("Modified successfully!!!")
        else:
            print("Not modified")

    elif choice==4:
        name=input("Enter name:")
        vehicle=vehicle_dict.get(name)
        if vehicle is not None:
            print("Vehicle:",vehicle)
        else:
            print("Wrong name.")

    elif choice==5:
        list_people=vehicle_dict.keys()
        print(list_people)

    elif choice==6:
        for k in vehicle_dict.keys():
            print(k)

    elif choice==7:
        for v in vehicle_dict.values():
            print(v)

    else:
        print("--------------Thankyou-------------")
