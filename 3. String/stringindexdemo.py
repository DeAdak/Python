s="This is cat, cat is cute, where is your cat"
print("count occurances cat",s.count("cat"))

#find (string to search,start,end)
pos=s.index("cat")
print("position: ",pos)
pos=s.index("cat",pos+1)
print("position: ",pos)
pos=s.index("cat",pos+1)
print("position: ",pos)
#if index does not find the string it throws exception
pos=s.index("cat",pos+1)
print("position: ",pos)
