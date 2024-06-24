from empdata import empList
from salariedemp import SalariedEmp
from contractemp import ContractEmp

def addEmployee(ch=0):
    eid = int(input("Enter employee ID: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    desg = input("Enter Designation: ")
    if ch==1:
        sal = float(input("Enter salary: "))
        empList.append(SalariedEmp(eid,name,dept,desg,sal))
        return True
    elif ch==2:
        hrsworked = int(input("Enter hours worked: "))
        hrcharges = float(input("Enter hourly charges: "))
        empList.append(ContractEmp(eid,name,dept,desg,hrsworked,hrcharges))
        return True
    return False

def displayAll():
    i=1
    for emp in empList:
        print(f"Employee-{i}:")
        print (emp)
        i+=1

def searchEmployee(eid):
    for emp in empList:
        if emp.get_eid()==eid:
            return emp
    return None
    
def deleteEmployee(eid=0):
    emp = searchEmployee(eid)
    if emp is not None:
        empList.remove(emp)
        return True
    return False

def modifySalary(eid,sal):
    emp = searchEmployee(eid)
    if isinstance(emp, SalariedEmp):
        emp.set_salary(sal)
        return True
    return False

def salarycalculate(eid):
    emp = searchEmployee(eid)
    if emp is not None:
        return emp.calculateSal()
    return None
   