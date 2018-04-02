#Emma Patton 2018-03-01
#Project Euler Problem 5
# https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

keeplooping = True
currentLCM = 2520

# currentLCM was changed from 1 to 2520 following further reading on: https://www.youtube.com/watch?v=EMTcsNMFS_g to reduce the number of checks 

while keeplooping:
    currentLCM = currentLCM + 2520

    howManyEven = 0 #Must be an even number to be counted (divisible with no remainder)

    for i in range(11, 21):

        if(currentLCM % i) == 0:
            howManyEven = howManyEven + 1


    if howManyEven == 10: #If all 10 numbers are even 
        keeplooping = False
        

print("The Lowest Common Multiple of numbers from 1 to 20 is:", currentLCM)
