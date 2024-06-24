from twowheeter import TwoWheeler
from threewheeler import ThreeWheeler
from fourwheeler import FourWheeler
from vehicledata import vehicleList

def addVehicle(ch):
    vid = int(input("Enter Vehical ID: "))
    name = input("Enter Vechal Name: ")
    vtype = input("Type - (LMV / HMV): ")
    price = float(input("Enter Price: "))
    petcap = int(input("Enter Petrol Capacity: "))
    if ch==1:
        chasis = input("Enter Chasis number: ")
        ans = input("Is Geared? (y/n): ")
        if ans=='y':
            var = int(input("No. of Gears: "))
            geared = True
        else:
            var = int(input("Consumption: "))
            geared = False
        vehicleList.append(TwoWheeler(vid,name,vtype,price,petcap,geared))
        if geared:
            vehicleList[-1].set_gearNum(var)
        else:
            vehicleList[-1].set_consumption(var)
        return True
    
    elif ch==2:
        seatNum = int(input("Enter Seat number: "))
        vehicleList.append(ThreeWheeler(vid,name,vtype,price,petcap,seatNum))
        return True
    elif ch==3:
        chasis = input("Enter Chasis number: ")
        engNum = input("Enter Engine Number: ")
        engPow = input("Enter engine Power: ")
        vehicleList.append(FourWheeler(vid,name,vtype,price,petcap,chasis,engNum,engPow))
        return True
    return False

def deleteVehicle(vid):
    vehh = None
    for veh in vehicleList:
        if veh.get_vid()==vid:
            vehh = veh
    if vehh is not None:
        vehicleList.remove(vehh)
        return True
    return False

def displayTwo():
    for veh in vehicleList:
        if isinstance(veh,TwoWheeler):
            print(veh)
            
def displayThree():
    for veh in vehicleList:
        if isinstance(veh,ThreeWheeler):
            print(veh)
            
def displayFour():
    for veh in vehicleList:
        if isinstance(veh,FourWheeler):
            print(veh)
            
def displayAll():
    for veh in vehicleList:
        print(veh)