##9. Write a function filter_long_words() that takes a list of words
##and an integer n and returns the list of words that are longer than n

def find_long_words(list1,n):
    list2=[]
    for x in list1:
        if len(x)>n:
            list2.append(x)

    return list2

list1 = ["Nishant","Ajay","Rahul","Ramakrishna","Krushnamohan","Ogyappa"]
n=int(input("Enter a interger: "))
print(f"list of words that are longer than {n}: {find_long_words(list1,n)}")
