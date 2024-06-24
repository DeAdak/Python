age=int(input("enter number"))
if age <5:
    print("you are in kindergarden")
    print("you are not eligible to drive car")
elif age>=5 and age<12:
    print("you are in primary school")
    print("you are not eligible to drive car")
elif age>=12 and age<18:
    print("you are in high school")
    print("you are not eligible to drive car")
elif age>=18 and age<21:
    print("you are in college")
    print("you are eligible to drive car")
else:
    print("you are now eligible to work and drive car")
