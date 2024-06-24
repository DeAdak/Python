import sys

def char_even(str1):
    return str1[::2]
def char_odd(str1):
    return str1[1::2]
def string_length(srt1):
    return len(str1)
def add_a(str1):
    return str1 + "a"*len(str1)
str1 = input("Enter the string: ")
ch=""
while ch!='e':
    print("-------------MENU--------------")
    print("a. display characters from even position")
    print("b. display characters from odd positionc.")
    print("c. display length of a string.")
    print("d. add a at the end of string length times.")
    print("e. exit")
    ch = input("choose option: ")
    if ch=='a':
        print("characters from even position: ",char_even(str1))
    elif ch=='b':
        print("characters from odd position: ",char_odd(str1))
    elif ch=='c':
        print("Length of the string: ",string_length(srt1))
    elif ch=='d':
        print("Result: ",add_a(str1))
    elif ch=='e':
        print("---------Thankyou----------")
    else:
        sys.exit(0)
