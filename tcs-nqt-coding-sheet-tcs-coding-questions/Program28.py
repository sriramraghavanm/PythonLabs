# Sum Of Digits of A Number
# Problem Statement: Given an integer, find the sum of digits of that integer.

number = int(input("Enter a number - "))
actualNumber = number
sum = 0
remainder = 0

while number != 0:
    remainder = int(number % 10)
    number = int(number / 10)
    sum = sum + remainder

print("Sum of digits of the number ", actualNumber, " is ", sum)