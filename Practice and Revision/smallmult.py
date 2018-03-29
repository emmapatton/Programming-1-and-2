# Emma Patton 2018-02-25
# Project Euler problem 5
# https://projecteuler.net/problem=5

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

found = False

counter = 0


while not found:

    counter = counter + 1

    for num in numbers:
        print(num, counter)
        if (counter % num) != 0:
            continue

        # if num is 20:
        #     found = True
        #     print(counter)


print('Done!')