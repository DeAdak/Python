s="This is cat, cat is cute, where is your cat"
print("count occurances cat",s.count("cat"))

#find (string to search,start,end)
pos=s.find("cat")
while pos!=-1:
    print("position: ",pos)
    pos=s.find("cat",pos+1)
    
##print("position: ",pos)
##pos=s.find("cat",pos+1)
##print("position: ",pos)
###if find doesnot found the string then it returns -1
##pos=s.find("cat",pos+1)
##print("position: ",pos)
##
##pos=s.find("dog")
##print("position of dog",pos)
