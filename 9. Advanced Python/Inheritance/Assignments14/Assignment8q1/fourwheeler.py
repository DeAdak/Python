from vehicle import Vehicle

class FourWheeler(Vehicle):
    
    def __init__(self,vid=0,name="",vtype="",price=0.0,petcap=0,chasis="",engNum="",engPow=""):
        super().__init__(vid,name,vtype,price,petcap)
        self.__chasis = chasis
        self.__engNum = engNum
        self.__engPow = engPow
        
    def __str__(self):
        return super().__str__()+f", Chasis No. : {self.__chasis}, Engine No. : {self.__engNum}, Engine Power : {self.__engPow}"
        
