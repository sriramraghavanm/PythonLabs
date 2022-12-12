# Program to find Sum of GP Series
# Problem Statement: Given a geometric Progression (G.P) sequence with some inputs as:-

# a, first term
# r, common ratio
# n, number of terms

# Example 1:
# Input: a=1 , r=0.5 , n=3
# Output: 1.75
# Explanation: The sum of given GP Series is 1.75

# Example 2:
# Input: a=3 , r=5 , n=2
# Output: 18
# Explanation: The sum of the given GP Series is 18

firstTerm = float(input("Enter the first term of the GP "))
commonRatio = float(input("Enter the common ratio of the GP "))
numberOfTerms = int(input("Enter the number of terms of the GP "))

# Approach - using formula sumOfGP = a * ((r ^ n - 1)/(r - 1))

sumOfGP = firstTerm * ((pow(commonRatio, numberOfTerms) - 1)/(commonRatio - 1))

print("Sum of the GP is ",sumOfGP)