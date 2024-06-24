from services import *

choice=0
while choice!=7:
    print("\n-----------------MENU-----------------")
    print("1. Add new Employee.")
    print("2. Delete employee.")
    print("3. Modify salary of employee.")
    print("4. Search employee.")
    print("5. Calculate Salary of Employee.")
    print("6. Display All.")
    print("7. Exit.")
    choice=int(input("Enter choice: "))
    
    if choice==1:
        print("1. Salaried Employee.")
        print("2. Contract Employee.")
        ch = int(input("choose option: "))
        if addEmployee(ch):
            print("Employee added successfully!!!")
        else:
            print("Employee not added.")
    
    elif choice==2:
        eid = int(input("Enter Employee ID: "))
        if deleteEmployee(eid):
            print("Employee Removed successfully!!!")
        else:
            print("Employee Not Found.")
    
    elif choice==3:
        eid = int(input("Enter Employee ID: "))
        sal = float(input("Enter new Salary: "))
        if modifySalary(eid,sal):
            print("Salary modified successfully!!!")
        else:
            print("Not a Salaried Employee.")
    
    elif choice==4:
        eid = int(input("Enter Employee ID: "))
        emp = searchEmployee(eid)
        if emp is None:
            print("Employee Not Found!!!!")
        else:
            print(emp)
    
    elif choice==5:
        eid = int(input("Enter Employee ID: "))
        sal = salarycalculate(eid)
        if sal:
            print("Salary is : ",sal)
        else:
            print("Employee not found!!!")
    
    elif choice==6:
        displayAll()
    
    elif choice==7:
        print("---------------Thankyou--------------------")
    
    else:
        print("Wrong Input!!!")