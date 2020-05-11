def factorial(num):

    count = 1
    for item in range(num, 1, -1): #range= num to 1
        count *= item
    return count


print(factorial(3)) #factorial num of 3 = 1*2*3!
print(factorial(4))  # factorial num of 3 = 1*2*3*4!
print(factorial(5))  # factorial num of 3 = 1*2*3*4*5!
