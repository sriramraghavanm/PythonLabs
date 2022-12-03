# Greatest of two numbers
# Problem Statement: Given two numbers. Find the greatest of two numbers.

# Example 1:
# Input: 1 3 5
# Output: 5
# Explanation: Answer is 5.Since 5 is greater than 1 and 3.

no1 = int(input("Enter number1 - "))
no2 = int(input("Enter number2 - "))
no3 = int(input("Enter number3 - "))

if (no1 == 0) and (no2 == 0) and (no3 == 0):
    print("All the numbers are 0")
elif no1 > no2 and no1 > no3:
    print(no1," is greater than ",no2," and ",no3)
elif no2 > no1 and no2 > no3:
    print(no2," is greater than ",no1," and ",no3)
else:
    print(no3," is greater than ",no1," and ",no2)

# Approach 2 - using max() function
print("Greatest of the three numbers is ", max(no1,no2,no3))