from vehicle import Vehicle

class ThreeWheeler(Vehicle):
    
    def __init__(self,vid=0,name="",vtype="",price=0.0,petcap=0,seatNum=0):
        super().__init__(vid,name,vtype,price,petcap)
        self.__seatNum = seatNum
        
    def __str__(self):
        return super().__str__()+f", Number of Seats : {self.__seatNum}"
        