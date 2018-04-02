# Emma Patton, 2018-04-02
# Python script that requests a single positive interger as an input 
# to find the factorial of that interger



def factorial(x):
    numx = 1
    for i in range(1, x + 1):
        numx = numx * i
    return numx


nString = input("Enter a positive whole number: ") #Using prior knowledge from problem set 3 (collatz.py) 
n = int(nString)

fact = factorial(n)
print("The factorial of", nString, "is:", fact)