from services import *

choice=0
while choice!=7:
    print("\n-----------------MENU----------------")
    print("1. add a new vehicle.\n2. delete the vehicle.\n3. display all 2 wheeler.\n4. display all 3 wheeler.\n5. display all 4 wheeler.\n6. display by id.\n7. exit")
    choice = int(input("Choose Option: "))
    
    if choice==1:
        print("1. 2 Wheeler.")
        print("2. 3 Wheeler.")
        print("3. 4 Wheeler.")
        ch = int(input("Choose Option: "))
        if addVehicle(ch):
            print("Vehicle added successfully!!!!")
        else:
            print("Vehicle not added!!!!")
    
    elif choice==2:
        vid = int(input("Enter vehicle ID: "))
        if deleteVehicle(vid):
            print("Vehicle deleted successfully!!!")
        else:
            print("Vehicle Not Found.")
    
    elif choice==3:
        displayTwo()
    
    elif choice==4:
        displayThree()
    
    elif choice==5:
        displayFour()
    
    elif choice==6:
        displayAll()
    
    elif choice==7:
        print("-------------------Thankyou--------------------")
    
    else:
        print("Wrong Choice!!!")
