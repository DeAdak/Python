##2. Write a version of a palindrome recognizer that also accepts phrase
##palindromes such as
##"Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets",
##"Sit on a potato pan, Otis", "Lisa Bonet ate no basil",
##"Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori",
##"Rise to vote sir", or the exclamation "Dammit, I'm mad!".
##Note that punctuation, capitalization, and spacing are usually ignored.


def check_palindrome(str1):
    str2=""
    for i in range(len(str1)):
        if str1[i].isalpha():
            str2 = str2 + str1[i].lower()

    str3 = str2[::-1].lower()
    if str2 == str3:
        return True
    else:
        return False

str1 = input("Enter your Phrase: ")

if check_palindrome(str1):
    print("Phrase is palindrome.")
else:
    print("Phrase is not Palindrome.")
    
