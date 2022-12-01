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

number = int(input("Enter a number - "))
temp = number
factorial = 1

# Approach 1 - using while loop
while temp != 0:
    factorial = factorial * temp
    temp = temp - 1
    
print("Using Iterative approach while loop: Factorial of the number ",number," is ",factorial)

# Approach 2 - using for loop
factorial = 1

for i in range(number):
    factorial = factorial * (i + 1)
print("Using Iterative approach for loop: Factorial of the number ",number," is ",factorial)