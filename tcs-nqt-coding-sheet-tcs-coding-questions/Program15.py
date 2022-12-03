# Reverse digits of a number
# Problem Statement: Given an integer. Write a program to reverse digits of a number.

# Example 1:
# Input: N = 472
# Output: 274
# Explanation: Reading the number from back to front, we see that the output should be 274

# Example 2:
# Input: N = 470
# Output: 74
# Explanation: Reading the number from back to front, we get 074. For an integer with no decimals, we know that leading zeros have no significance and therefore our answer should be 74

no = int(input("Enter a number "))

actualNo = no
remainder = 0
rev = 0

if actualNo == 0:
    print("Reverse is 0")
else:
    while actualNo != 0:
        remainder = int(actualNo % 10)
        actualNo = int(actualNo / 10)
        rev = rev * 10 + remainder
    print("Reverse of ",no," is ",rev)