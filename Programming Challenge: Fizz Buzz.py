two_input=range(1,51)
for num in two_input:

    if num % 3 == 0 and num % 5 == 0: # If num is divisible by both 3 and 5, "FizzBuzz" will be printed.
        print("FizzBuzz")

    elif num % 3 == 0:# If num is only divisible by 3, "Fizz" will be printed.
        print("Fizz")

    elif num % 5 == 0:# If num is only divisible by 5, "Buzz" will be printed.
        print("Buzz")

    else:
        print(num)# num itself will be printed in all other cases.
