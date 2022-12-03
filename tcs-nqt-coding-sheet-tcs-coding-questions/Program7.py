# Check whether a given number is even or odd
# Problem Statement: Given a number n, check whether a given number is even or odd.

# Example 1:
# Input: n=5
# Output: odd
# Explanation: 5 is not divisible by 2.
 
# Example 2:  
# Input: n=6
# Output: even
# Explanation: 6 is divisible by 2.

no = int(input("Enter a number "))

if no % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")