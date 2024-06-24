from employee import Employee

class ContractEmp(Employee):
    
    def __init__(self,eid=0,name="",dept="",desg="",hrsworked=0,hrcharges=0):
        super().__init__(eid,name,dept,desg)
        self.__hrsWorked = hrsworked
        self.__hourlyCharges = hrcharges
        
    def __str__(self):
        return super().__str__()+f", Hours Worked : {self.__hrsWorked}, Hourly Charges : {self.__hourlyCharges}"
    
    def set_hrsWorked(self,hrsworked=0):
        self.__hrsWorked = hrsworked
        
    def set_hourlyCharges(self,hrcharges=0):
        self.__hourlyCharges = hrcharges
        
    def get_hrsWorked(self):
        return self.__hrsWorked
    
    def get_hourlyCharges(self):
        return self.__hourlyCharges
    
    def calculateSal(self):
        return self.__hourlyCharges * self.__hrsWorked