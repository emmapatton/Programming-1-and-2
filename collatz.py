#Emma Patton, 2018-02-11
#The Collatz Conjecture Program: https://en.wikipedia.org/wiki/Collatz_conjecture

nString = input("Enter a number: ")
n = int(nString)
 
count = 0
print("starting value:", n)

while n != 1:

    if(n % 2 == 0):
        n = int(n / 2)
    else:
        n = int(3 * n + 1)

    print(n)
    count = count + 1


print('Program finished in', count, 'steps')
    
