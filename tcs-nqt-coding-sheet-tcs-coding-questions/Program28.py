# Sum Of Digits of A Number
# Problem Statement: Given an integer, find the sum of digits of that integer.

# Example 1:
# Input: N = 472
# Output: 13
# Explanation: The digits in the number are 4,7 and 2. Summing them up gives us a value of 13

# Example 2:
# Input: N = 102
# Output: 3
# Explanation: The digits in the number are 0, 1, and 2. Summing them up gives us a value of 3

number = int(input("Enter a number - "))
actualNumber = number
sum = 0
remainder = 0

if number <= 0:
    print("Number should be greater than 0")
else:
    while number != 0:
        remainder = int(number % 10)
        number = int(number / 10)
        sum = sum + remainder

    print("Sum of digits of the number ", actualNumber, " is ", sum)