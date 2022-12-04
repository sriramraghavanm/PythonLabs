# Factorial of a Number : Iterative and Recursive
# Problem Statement: Given a number X,  print its factorial.

# Example 1:
# Input: X = 5
# Output: 120
# Explanation: 5! = 5*4*3*2*1

# Example 2:
# Input: X = 3
# Output: 6
# Explanation: 3!=3*2*1
import math

number = int(input("Enter a number - "))
temp = number
factorial = 1

def calculate_factorial(n):
    if n == 1:
        return n
    else:
        return n * calculate_factorial(n-1)

# 0! is always 1
if number == 0:
    print("Factorial of the number ",number," is ",factorial)
elif number < 0:
    print("Factorial of ",number," is not defined")
# Approach 1 - using while loop
else:
    while temp != 0:
        factorial = factorial * temp
        temp = temp - 1
    print("Using Iterative approach while loop: Factorial of the number ",number," is ",factorial)

    # Approach 2 - using for loop
    factorial = 1

    for i in range(number):
        factorial = factorial * (i + 1)
    print("Using Iterative approach for loop: Factorial of the number ",number," is ",factorial)

    # Approach 3 - using math.factorial function
    print("Using function: Factorial of the number ",number," is ",math.factorial(number))

    # Approach 4 - using recursion
    print("Using Recursion approach : Factorial of the number ",number," is ",calculate_factorial(number))