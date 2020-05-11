var1= int(input("Enter an integer 'C 'value that you want to convert to 'F' value"))

def C_to_fahren(var1):
    F = 1.8 *var1 + 32
    return round(F,2)

print("The Fahrenheit equivalent of " + str(var1) +" degrees Celsius is "+ str(C_to_fahren(var1))) #since we can't concatinate str with int, var1 and function have to convert into str
