##4. Write a function translate() that will translate a text into
##"rövarspråket" (Swedish for "robber's language").
##That is, double every consonant and place an occurrence of "o" in between.
##For example, translate("this is fun") should return the string
##"tothohisos isos fofunon".

def translate(str1):
    str2 = ""
    for i in range(len(str1)):
        if str1[i].lower() in ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]:
            str2 = str2 + str1[i]+"o"+str1[i]
        else:
            str2 = str2 + str1[i]
    return str2

str1 = input("Enter string: ")

print("Translated string: ",translate(str1))
