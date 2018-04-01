#Emma Patton, 2018-02-11
#The Collatz Conjecture Program: https://en.wikipedia.org/wiki/Collatz_conjecture

nString = input("Enter a number: ") #input function added following reading from (point 1.10.1): https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/io.html
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

# Number of iterations printed following reading from: https://www.pythonlearn.com/html-008/cfbook006.html 
    
