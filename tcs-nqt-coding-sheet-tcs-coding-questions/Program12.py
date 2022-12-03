# Greatest of two numbers
# Problem Statement: Given two numbers. Find the greatest of two numbers.

# Example 1:
# Input: 1 3
# Output: 3
# Explanation: Answer is 3,since 3 is greater than 1.

no1 = int(input("Enter number1 - "))
no2 = int(input("Enter number2 - "))

if (no1 == 0) and (no2 == 0):
    print("Both the numbers are 0")
elif no1 == no2:
    print("Both the numbers are same")
elif no1 > no2:
    print(no1, " is greater than ", no2)
else:
    print(no2, " is greater than ", no1)

# Approach 2 - using max() function
print("Greatest of the two numbers is ", max(no1,no2))