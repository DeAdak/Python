import sys
#add vehicle in the list
def addVehicle():
    v=input("new vehicle name")
    if v in lst:
        ch=input("The vehicle exists, still you want to add it?(y/n)")
        if ch=='y':
           lst.append(v)
    else:
        lst.append(v)
        
def displayAllVehicle():
    for v in lst:
        print(v,end=",")
    print()

def deleteVehicle(ch,data):
    if ch==1:
        if data<len(lst):
            lst.pop(data)
            return True
        else:
            return False
    else:
        if data in lst:
            lst.remove(data)
            return True
        else:
            return False
def searchByName(veh):
    if veh in lst:
        pos=lst.index(veh)
        return pos
    else:
        return -1
    
def searchByPosition(pos):
    if pos <len(lst):
        return lst[pos]
    else:
        return None
    
def modifyVehicle(veh,nveh):
    pos=searchByName(veh)
    if pos!=-1:
        ans=input(f"do you want to overwrite {veh} by {nveh}")
        if ans=='y':
            lst[pos]=nveh
            return 1
        else:
            return 2
    else:
        return 3
        

lst=[]
choice=0
while choice !=7:
      print("1. add new vehicle \n2.delete the vehicle\n3. modify vehicle name")
      print("4. search by name\n 5.search by position\n 6.display all vehicles\n 7.exit")
      choice=int(input("enter choice: "))
      if choice==1:
          addVehicle()
      elif choice==2:
          print("1.delete by position\n 2. delete by name")
          ch=int(input("choice: "))
          if ch==1:
              data=int(input("enetr position to delete"))
          else:
              data=input("enter vehicle name to delete")
                
          status=deleteVehicle(ch,data)
          if status:
              print(f"{data} deleted")
          else:
              print(f"{data} not deleted")
      elif choice==3:
          veh=input("enter vehicle name to modify")
          nveh=input("enter vehicle name to modify")
          status=modifyVehicle(veh,nveh)
          if status==1:
              print(f"{veh} name is modified to {nveh} is done")
          elif status==2:
            print(f"{veh} found but not modified to {nveh}")
          else:
              print(f"{veh} not found")
              
      elif choice==4:
          veh=input("enter vehicle name to search")
          pos=searchByName(veh)
          if pos!=-1:
              print(f"{veh} found at {pos} position")
          else:
              print(f"{veh} not found")
      elif choice==5:
           pos=int(input("enetr position to search"))
           veh=searchByPosition(pos)
           if veh==None:
               print(f"vehicle not found at {pos} position")
           else:
               print(f"{veh}  found at {pos} position")
      elif choice==6:
          displayAllVehicle()
      elif choice==7:
          print("Thank you for using the program, do visit again....")
          #sys.exit(0)
      else:
          print("wrong choice")
