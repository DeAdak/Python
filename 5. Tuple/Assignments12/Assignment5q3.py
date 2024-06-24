import sys

def add_data(list1,data,ch):
    if ch=='a':
        list1.append(data)
    else:
        pos = int(input("Enter position: "))
        list1.insert(pos,data)

def display_data(list1,ch):
    if ch=='a':
        return list1
    else:
        return [x for x in enumerate(list1)]

def delete_value(list1,value):
    if value in list1:
        list1.remove(value)
        return True
    return False

def delete_pos(list1,pos):
    if len(list1)>pos:
        value = list1.pop(pos)
        return True
    return False

def sort_list(list1,ch):
    if ch=='a':
        list1.sort()
        return list1
    else:
        list1.sort(reverse=True)
        return list1
    
list1=[25,85,85,78,55.89]
choice=0
while choice!=9:
    print("------------MENU--------------")
    print("1. Accept Data")
    print("2. Delete data by value")
    print("3. delete data by position")
    print("4. sort")
    print("5. reverse")
    print("6. Print in sorted order without changing original list")
    print("7. print in reverse order without changing original list")
    print("8. display data")
    print("9. Exit.")
    choice = int(input("Choose a Option: "))

    if choice==1:
        print("a) add at last position.")
        print("b) add at given position.")
        ch = input("Choose option: ")
        if ch in ['a','b']:
            data = int(input("Enter data: "))
            add_data(list1,data,ch)
            print("Data added successfully!!!")
        else:
            print("invalid input.")

    elif choice==2:
        value = int(input("Enter data: "))
        if delete_value(list1,value):
            print("Deleted successfully!!!")
        else:
            print("data not found")
            
    elif choice==3:
        pos = int(input("Enter position: "))
        if delete_pos(list1,pos):
            print("Deleted successfully!!!")
        else:
            print("data not found")
            
    elif choice==4:
        print("a) ascending")
        print("b) descending")
        ch = input("Choose option: ")
        if ch in ['a','b']:
            print("Sorted data: ",sort_list(list1,ch))
        else:
            print("invalid input.")
            
    elif choice==5:
        list1.reverse()
        print(list1)
        
    elif choice==6:
        for x in sorted(list1):
            print(x)
        
    elif choice==7:
        for x in reversed(list1):
            print(x)

    elif choice==8:
        print("a) normal")
        print("b) numbered")
        ch = input("Choose option: ")
        if ch in ['a','b']:
            print(display_data(list1,ch))
        else:
            print("invalid input.")

    elif choice==9:
        print("----------Thankyou-----------")

    else:
        sys.exit(0)
