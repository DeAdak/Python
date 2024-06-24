##8. Write a function find_longest_word() that takes a list of words
##and returns the length of the longest one.

def find_longest_word(list1):
    length=0
    for x in list1:
        if len(x)>length:
            length=len(x)

    return length

list1 = ["Nishant","Ajay","Rahul","Ramakrishna","Krushnamohan","Ogyappa"]
print("Length of longest word is: ",find_longest_word(list1))
