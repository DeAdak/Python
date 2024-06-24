##3. A pangram is a sentence that contains all the letters of the
##English alphabet at leastonce,
##for example: The quick brown fox, jumps over the lazy dog !!!!.
##Your task here is to write a function to check a sentence to see if it is a
##pangram or not.

def pangram(str1):
    strset = set()
    #print(type(strset))
    for x in range(len(str1)):
        if str1[x].isalpha():
            strset.add(str1[x].lower())
    if len(strset)==26:
        return True
    else:
        return False
str2 = "The quick brown fox, jumps over the lazy dog !!!!."
str1 = input("Enter a sentence to check for pangram: ")
if pangram(str1):
    print("The given sentence is pangram.")
else:
    print("The given sentence is not pangram.")
             
