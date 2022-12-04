# Sum of first N Natural Numbers
# Problem statement: Given a number ‘N’, find out the sum of the first N natural numbers.
# Natural numbers are the numbers that start from 1 and end at infinity.

# Example 1:
# Input: N=5
# Output: 15
# Explanation: 1+2+3+4+5=15

# Example 2:
# Input: N=6
# Output: 21
# Explanation: 1+2+3+4+5+6=15

n = int(input("Enter a number - "))

sum = 0

if n <= 0:
    print("Enter a value greater than 0")
else:
    for i in range(n + 1):
        sum = sum + i

    print("Sum of first ",n," natural numbers is ",sum)

    # Approach 2 - Second approach using the formula, n = n(n+1)/2

    sum = int(n * (n + 1)/2)

    print("Using Formula  method : Sum of first ",n," natural numbers is ",sum)