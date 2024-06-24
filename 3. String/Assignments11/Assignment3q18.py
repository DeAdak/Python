##11. In English, present participle is formed by adding suffix -ing to infinite form: go -> going.
## A simple set of heuristic rules can be given as follows: 
## If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.) 
## If the verb ends in ie, change ie to y and add ing For words consisting of consonant-vowel-consonant, 
## double the final letter before adding ing By default just add ing
##Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form
##returns its present participle form. Test your function with words such as lie, see, move and hug.


def make_ing_form(word="default"):
    vov = ['a','e','i','o','u']
    if word.endswith("ie"):
        return word[:-2]+"ying"
    elif word.endswith("e"):
        return word[:-1]+"ing"
    elif (word[-3] not in vov) and (word[-2] in vov) and (word[-1] not in vov):
        return word + word[-1] + "ing"
    else:
        return word+"ing"

ch='y'    
while ch=='y':
    word = input("Enter a word: ")
    print("Present participle is: ", make_ing_form(word))
    ch=input("want to Continue?(y/n): ")
