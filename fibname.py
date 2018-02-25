# Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.
# Modified by Emma Patton 2018-02-04

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i = j
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Patton"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)


# Week 1 Discussion Forum Post: 
# My name is Emma. The first and last letters of my name (E + A = 5 + 1) give the number 6. The 6th Fibonacci number is 8. 


# Week 2 Discussion Forum Post:
# My surname is Patton
# The first letter P is number 80
# The last letter n is number 110
# Fibonacci number 190 is 784637716923335095479473677900958302012794430558004314112

# ord() is a Python built in function. It returns the integer representing a Unicode character. 
