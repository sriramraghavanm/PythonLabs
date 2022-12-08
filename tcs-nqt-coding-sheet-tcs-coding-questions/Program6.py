# Check whether a number is Perfect Number or not
# Problem Statement: Perfect Number. Write a program to find whether a number is a perfect number or not.
# A perfect number is defined as a number that is the sum of its proper divisors ( all its positive divisors excluding itself). 

# Example 1:
# Input: n=6
# Output: 6 is a perfect number

# Example 2:
# Input: n=15
# Output: 15 is not a perfect number

# Example 3:
# Input: n=28
# Output: 28 is a perfect number
# Reason:
# For 6 and 28 , the sum of their proper divisors (1+2+3) and (1+4+7+14) is equal to the respective numbers and for 15 it is not.

# Approach 1 - using for loop

no = int(input("Enter a number "))

sum = 0

for i in range(no):
    i = i + 1
    if no % i == 0 and no != i:
        sum = sum + i

if sum == no:
    print(no, " is a perfect number")
else:
    print(no, " is not a perfect number")