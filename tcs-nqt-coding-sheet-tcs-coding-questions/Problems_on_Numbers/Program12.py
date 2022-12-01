# Greatest of two numbers
# Problem Statement: Given two numbers. Find the greatest of two numbers.

no1 = int(input("Enter number1 - "))
no2 = int(input("Enter number2 - "))

if no1 > no2:
    print(no1, " is greater than ", no2)
else:
    print(no2, " is greater than ", no1)

# Approach 2 - using max() function
print("Greatest of the two numbers is ", max(no1,no2))