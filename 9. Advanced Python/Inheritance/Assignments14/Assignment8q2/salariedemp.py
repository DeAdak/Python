from employee import Employee

class SalariedEmp(Employee):
    
    def __init__(self,eid=0,name="",dept="",desg="",sal=0):
        super().__init__(eid,name,dept,desg)
        self.__salary = sal
        self.__bonus = sal*20/100
        
    def __str__(self):
        return super().__str__()+f", Salary : {self.__salary}, Bonus : {self.__bonus}"
    
    def set_salary(self,sal=0):
        self.__salary = sal
        self.__bonus = sal*20/100
        
    def get_salary(self):
        return self.__salary
    
    def get_bonus(self):
        return self.__bonus
    
    def calculateSal(self):
        Da = self.__salary*10/100
        Hra = self.__salary*15/100
        Pf = self.__salary*8/100
        Net_sal = self.__salary + Da + Hra - Pf
        return Net_sal
        
    