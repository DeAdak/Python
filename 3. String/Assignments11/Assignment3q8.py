##1. Define a procedure histogram() that takes a list of integers and
##prints a histogram to the screen. For
##example, histogram([4, 9, 7]) should print the following:
##****
##*********
##*******

def histogram(lst=[4, 9, 7]):
    for i in range(len(lst)):
        print("*"*lst[i])

lst = [5,7,6,9]
histogram(lst)
