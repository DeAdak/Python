choice=0;
courses={'DBDA':65,'DAI':120}
def addnewcourse():
    cname=input("enetr course name")
    num=int(input("enetr number"))
    v=courses.get(cname,-1)
    if v==-1:   #add key value is key not exists
        courses[cname]=num
        return 1
    else:
        ans=input("key exists overwrite(y/n)")
        if ans=='y': #overwrite key value is key  exists
            courses[cname]=num
            return 2
        else:
            return 3
        


def deletecourse(cnm):
    # it is better to show details to user and ask are you sure
    status=courses.pop(cnm,False)
    if status!=False:
        return True
    else:
        return False
    
def displayAll():
    for k,v in courses.items():
        print(k,"---->",v)
        
def displaybynum(num):
    for k,v in courses.items():
        if v > num:
            print(k,"---->",v)
def updatenumber(cnm,num):
    if cnm in courses:
        print("Current details :")
        
        print(cnm,courses[cnm])
        ans=input("are you sure(y/n)")
        if ans=='y':
            courses[cnm]=num
            return True
        else:
            return False
    else:
        return False
    
while choice!=6:
    print("1.add new course\n2.delete the course\n3.modify course\n4.display all\n")
    print("5. display all courses with number of students > given number\n6.exit")
    choice=int(input("enetr choice"))
    if choice==1:
        status=addnewcourse()
        if status==1:
            print("new course added")
        elif status==2:
            print("course value overwritten")
        else:
            print("course exists so not overwritten")
    elif choice==2:
        cnm=input("enetr course to delete")
        status=deletecourse(cnm)
        if status:
            print("course deleted")
        else:
            pint("not deleted / not found")
    elif choice==3:
        cnm=input("enetr course to modify number of students")
        nnum=int(input("enter new number of student"))
        status=updatenumber(cnm,nnum)
        if status:
            print("updation done")
        else:
            print("updatetion not done")
    elif choice==4:
        displayAll()
    elif choice==5:
        num=int(input("enetr number"))
        displaybynum(num)
    elif choice==6:
       print("Thank you for visiting .....")
    else:
        print("wrong choice")
      
