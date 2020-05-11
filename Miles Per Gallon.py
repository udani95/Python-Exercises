from random import randint

gallons=randint(10,25) #this will choose random any num between 10, 25
miles=randint(200,400) #this will choose random any num between 200, 400

print("The miles per gallons(MOG) = "+str(gallons/miles))
print("The gallons of gas in the car = " + str(gallons))
print("The miles that the car can travel = ",str(miles))
