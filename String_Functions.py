mixed_case ="A Song of Ice and Fire"
print(mixed_case.isupper()) #see whether all letters are capital or not
print(mixed_case.islower()) #see whether all letters are simple or not

print(mixed_case.upper()) #Converting string of all upper case letters
print(mixed_case.lower()) #Converting string of all lower case letters
print(mixed_case.istitle()) #see whether all words 1st letter is capital or not

title_case = mixed_case.title()
print(title_case)
print(mixed_case.startswith("A")) #print true if the string start with A
print(mixed_case.endswith("e"))  #print true if the string end with e

words=mixed_case.split(" ") #splitting the string
print(words)

test= " ".join(words) #joining the splitted words into a string
print(test)
print(test.isalpha())
