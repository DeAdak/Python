class Person:
    
    def __init__(self,eid=0,name=""):
        self.__eid = eid
        self.__name = name
    
    def __str__(self):
        return f"ID : {self.__eid}, Name : {self.__name}"

    def set_eid(self,eid=0):
        self.__eid = eid
        
    def set_name(self,name=""):
        self.__name = name
        
    def get_eid(self):
        return self.__eid
    
    def get_name(self):
        return self.__name