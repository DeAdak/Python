from twowheeter import TwoWheeler
from threewheeler import ThreeWheeler
from fourwheeler import FourWheeler

vehicleList = []

v1 = TwoWheeler(123,"Hornet","LMV",110000.0,10,"ABC75869",True)
v1.set_gearNum(5)
v2 = TwoWheeler(124,"Activa","LMV",125000.0,25,"HGBH78564",False)
v2.set_consumption(25)
v3 = ThreeWheeler(125,"Auto","LMV",200000.0,25,4)
v4 = ThreeWheeler(126,"AutoX","HMV",250000.0,30,6)
v5 = FourWheeler(120,"Honda City","HMV",1500000.0,50,"FSFJ564354","456231","252")
v6 = FourWheeler(121,"Amaze","LMV",850000.0,40,"HNJU5354","582364","100")

vehicleList.append(v1)
vehicleList.append(v2)
vehicleList.append(v3)
vehicleList.append(v4)
vehicleList.append(v5)
vehicleList.append(v6)


