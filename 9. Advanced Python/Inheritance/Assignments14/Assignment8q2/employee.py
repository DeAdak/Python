from person import Person
from abc import ABC,abstractmethod

class Employee(Person,ABC):
    
    def __init__(self,eid=0,name="",dept="",desg=""):
        super().__init__(eid,name)
        self.__department = dept
        self.__designation = desg
    
    def __str__(self):
        return super().__str__()+f", Department : {self.__department}, Designation : {self.__designation}"

    def set_department(self,dept=""):
        self.__department = dept
        
    def set_designation(self,desg=""):
        self.__designation = desg
        
    def get_department(self):
        return self.__department
    
    def get_designation(self):
        return self.__designation
    
    @abstractmethod
    def calculateSal(self):
        pass