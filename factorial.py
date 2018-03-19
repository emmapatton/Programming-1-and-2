# Emma Patton, 2018-03-19
# Python script containing a function called factorial() that 
# takes a single input/argument which is a positive integer 
# and returns its factorial. The factorial of a number is that 
# number multiplied by all of the positive numbers less than it. 

def factorial(x):
    numx = 1
    for i in range(1, x + 1):
        numx = numx * i
    return numx

print("The factorial of the value 5 is:", factorial(5))
print("The factorial of the value 7 is:", factorial(7))
print("The factorial of the value 10 is:", factorial(10))
