import sys

def delete_name(set1,ch):
    if ch=='a':
        set1.pop()
        return True
    else:
        name=input("Enter name to delete: ")
        if name in set1:
            set1.discard(name)
            return True
        return False
    
set1=set()
set2=set()
choice=0
while choice!=9:
    print("---------------MENU-----------------")
    print("1. Delete a element if exists otherwise do not show any errr.")
    print("2. Add a element.")
    print("3. Create one more set.")
    print("4. Union of 2 sets.")
    print("5. Intersection of 2 sets.")
    print("6. Difference of 2 sets.")
    print("7. Convert set into frozenset.")
    print("8. Display sets.")
    print("9. exit")
    choice=int(input("Choose option: "))
    if choice==1:
        if set1:
            print("a. Delete random name.")
            print("b. Detele specific name.")
            ch=input("Choose Option: ")
            if ch in ['a','b']:
                if delete_name(set1,ch):
                    print("Name deleted successfully!!!")
                else:
                    print("Name not deleted.")
            else:
                print("Invalid Input.")
        else:
            print("Set is empty.")
        
    elif choice==2:
        name=input("Enter Name: ")
        set1.add(name)
        print("Name added!!!")

    elif choice==3:
        ch='y'
        while ch=='y':
            name=input("Enter name: ")
            set2.add(name)
            ch=input("Want to add more?(y/n): ")

    elif choice==4:
        print("Union of 2 sets: ",set1|set2)

    elif choice==5:
        print("Intersection of 2 sets: ",set1&set2)

    elif choice==6:
        print("Difference of 2 sets: ",set1-set2)

    elif choice==7:
        set3=frozenset(set1)
        print("Frozen set: ",set3)

    elif choice==8:
        if set1:
            print("Set1: ",set1)
        if set2:
            print("Set2: ",set2)
    
    elif choice==9:
        print("--------------Thankyou-------------")

    else:
        sys.exit(0)
