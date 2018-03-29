# Emma Patton, 2018-03-02
# Formatting output

for i in range(1, 11):
    print('{:2d} {:3d} {:4d} {:5d}'.format(i, i**2, i**3, i**4))

a = 5
print(f'The value of a is {a} and a+1 is {a+1}.')

for i in range(1, 11):
    print(f'{i:2d} {i**2:3d} {i**3:4d} {i**4:5d}')


