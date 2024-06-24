class Vehicle:
    
    def __init__(self,vid=0,name="",vtype="",price=0.0,petcap=0):
        self.__vid = vid
        self.__name = name
        self.__vtype = vtype
        self.__price = price
        self.__petrolCapacity = petcap
        
    def __str__(self):
        return f"ID : {self.__vid}, Name: {self.__name}, Type: {self.__vtype}, Price: {self.__price}, Petrol Capacity: {self.__petrolCapacity}"

    def get_vid(self):
        return self.__vid