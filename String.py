#"String" in python

#How to write a string in python and print it
var1 = "This is how to write a string "
print(var1)

#Each of the charactor in the string belong to a  index number

var2 = "Index Number"
print("Character in (Index Number) index 3=",var2[3]) #To get and print the character in index 3(Note that initial character is starting from index 0)
    #or
print("Character in (Apple) index 0=","Apple"[0]) #To print the character in index 0

#String Slicing

var3 = "Slicing"
print("Sliced string (Slicing) from index 0-3= ",var3[:3]) #Print the sliced string from index 0-3
print("Sliced string (Slicing) from index 2-5= ",var3[2:5]) #Print the sliced string from index 2-5
print("Sliced string (Slicing) from index 4 to end= ",var3[4:]) #Print the sliced string from index 4 to end index

#String Concatination

var4= "This"
var5= "is"
var6= "String"
var7= "Concatination"
concat= var4 +var5 +var6+var7
print(concat)
print(concat[5])
print(concat[0:12])
