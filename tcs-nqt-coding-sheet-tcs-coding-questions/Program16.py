# Maximum and Minimum Digit in a Number
# Problem Statement: Given a number N, print the smallest and largest digits present in the number.

# Example 1:
# Input: N = 2746
# Output: Largest digit: 7
#        Smallest digit: 2
# Explanation: By simply going through the digits of the number, we figure out the largest and smallest digit in the number.

# Example 2:
# Input: N = 23004
# Output: Largest digit : 4
#        Smallest digit : 0
# Explanation: By simply going through the digits of the number, we figure out the largest and smallest digit in the number.

num = int(input("Enter a number "))

# This method will return the biggest digit of a number
def getBiggestDigit(n):
    max = 0
    while n != 0:
        remainder = int(n % 10)
        n = int(n / 10)
        if remainder > max:
            max = remainder
    return max
    
# This method will return the smallest digit of a number    
def getSmallestDigit(n,m):
    while n != 0:
        remainder = int(n % 10)
        n = int(n / 10)
        if remainder < m:
            m = remainder
    return m
    
max = getBiggestDigit(num)
min = getSmallestDigit(num, max)

print("Largest digit : ",max)
print("Smallest digit : ",min)