import sys
city_tree={'Pune':['Nilgiri','Coconut'],'Nagpur':['Orange','Sugercane']}

def add_detail(city,list1):
    if list1 == city_tree.setdefault(city,list1):
        return True
    print("City already exist!!!")
    return False

def delete_city(city):
    if city in city_tree:
        ch = input("Do you want to delete?(y/n)")
        if ch=='y':
            city_tree.pop(city)
            return True
        else:
            return False
    print("City not found")
    return False

def modify_city(city,list1):
    list2=city_tree.setdefault(city,list1)
    if list1==list2:
        return True
    city_tree.get(city).extend(list1)
    return True
    

choice=0
while choice!=7:
    print("\n--------------MENU-------------------")
    print("1. Add new city and trees commonly found in the city.")
    print("2. Display all cities and the list of trees for all cities.")
    print("3. Display list of trees of a particular city.")
    print("4. Display cities which have the given tree.")
    print("5. Delete city.")
    print("6. Modify tree list.")
    print("7. Exit.")
    choice=int(input("Enter your option:"))

    if choice==1:
        city=input("Enter city:")
        str1=input("Enter trees with space in between:")
        list1=str1.split()
        if add_detail(city,list1):
            print("City and Trees added Successfully!!!")
        else:
            print("Not added!!.")

    elif choice==2:
        print("City\t  Trees")
        for k,v in city_tree.items():
            print(k,"\t:",v)

    elif choice==3:
        city=input("Enter city:")
        list1=city_tree.get(city)
        if list1 is not None:
            print("Trees: ",list1)
        else:
            print("City not found!!!!")

    elif choice==4:
        tree=input("Enter tree:")
        print("Cities are:")
        for city,trees in city_tree.items():
            if tree in trees:
                print(city)
            
    elif choice==5:
        city=input("Enter city:")
        if delete_city(city):
            print("City deleted successfully!!!")
        else:
            print("City not deleted")

    elif choice==6:
        city=input("Enter city:")
        str1=input("Enter trees with space in between:")
        list1=str1.split()
        if modify_city(city,list1):
            print("Trees modified successfully!!")
        else:
            print("Not modified!!!")

    elif choice==7:
        print("---------------Thankyou----------------")
    else:
        print("Wrong Option")
        sys.exit(0)
