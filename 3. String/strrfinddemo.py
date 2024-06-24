s="This is cat, cat is cute, where is your cat"
print("count occurances cat",s.count("cat"))

#find (string to search,start,end)
pos=s.rfind("cat")
print("position from reverse side :",pos) 
pos=s.rfind("cat",0,pos-1)
print("position from reverse side :",pos) 
pos=s.rfind("cat",0,pos-1)
print("position from reverse side :",pos)
pos=s.rfind("cat",0,pos-1)
print("position from reverse side :",pos)
pos=s.rfind("cat",0,pos-1)
print("position from reverse side :",pos)
