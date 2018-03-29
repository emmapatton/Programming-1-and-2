# Emma Patton, 2018-03-19
# Learning about functions

def sumall(upto):
    sumupto = 0 
    for i in range(1, upto + 1):
        sumupto = sumupto + i
    return sumupto 

print("The sum of the values from 1 to 50 inclusive are:", sumall(50))

print("The sum of the values from 1 to 5 inclusive are:", sumall(5))

print("The sum of the values from 1 to 10 inclusive are:", sumall(10))


#Delete these lines of code - not needed with above (keep for learning for now)

sum5 = 0
for i in range(1, 6):
    sum5 = sum5 + i
print("The sum of the values from 1 to 5 inclusive are:", sum5)


sum10 = 0
for i in range(1, 11):
    sum10 = sum10 + i
print("The sum of the values from 1 to 10 inclusive are:", sum10)


#Learning about functions with GCD

def gcd(x, y):
    while x != 0 and y !=0:
        if x > y:
            x = x % y 
        else:
            y = y % x
    if x == 0:
        return y
    else: 
        return x

print("GCD of 6 and 15:", gcd(6,15))

z = gcd(221, 323)
print("GCD of 221 and 323:", z)

