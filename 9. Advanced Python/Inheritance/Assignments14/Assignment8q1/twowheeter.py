from vehicle import Vehicle

class TwoWheeler(Vehicle):
    
    def __init__(self,vid=0,name="",vtype="",price=0.0,petcap=0,chasis="",geared=False):
        super().__init__(vid,name,vtype,price,petcap)
        self.__chasis = chasis
        self.__geared = geared
        self.__gearNum = 0
        self.__consumption = 0
        
    def set_gearNum(self,gearNum):
        self.__gearNum = gearNum
        
    def set_consumption(self,con):
        self.__consumption = con
        
    def get_geared(self):
        return self.__geared
    
    def __str__(self):
        if self.__geared:
            return super().__str__()+f", Number of Gears : {self.__gearNum}"
        return super().__str__()+f", Consumption : {self.__consumption}"
