#Emma Patton 2018-03-01
#Project Euler Problem 5
# https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

keeplooping = True
currentLCM = 1

while keeplooping:
    currentLCM = currentLCM + 1

    howManyEven = 0

    for i in range(1, 21):

        if(currentLCM % i) == 0:
            howManyEven = howManyEven + 1


    if howManyEven == 20:
        keeplooping = False
        

print("Lowest Common Multiple is:", currentLCM)
