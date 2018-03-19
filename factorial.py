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

num = input("Please enter a positive number:")

num = int(num)

print(f"The factorial of the value {num} is:", factorial(num))

