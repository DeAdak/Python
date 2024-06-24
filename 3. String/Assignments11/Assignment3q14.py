##7. Define a function overlapping() that takes two lists and returns True
##if they have at least one
##member in common, False otherwise.

def overlapping(list1,list2):
    for x in list1:
        for y in list2:
            if x == y:
                return True
    return False

list1 = [23,56,45,78,88,"a","c"]
list2 = ["f","g","c",24,45,72]

if overlapping(list1,list2):
    print("Overlapping..")
else:
    print("Not overlapping..")
