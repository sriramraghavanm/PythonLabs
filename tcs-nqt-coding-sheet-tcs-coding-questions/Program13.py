# Greatest of three numbers
# Problem Statement: Given three numbers. Find the greatest of three numbers.

no1 = int(input("Enter number1 - "))
no2 = int(input("Enter number2 - "))
no3 = int(input("Enter number3 - "))

if (no1 > no2) & (no2 > no3):
    print(no1, " is greater than ", no2)
elif (no2 > no3) & (no2 > no1):
    print(no2, " is greater than ", no3)
else:
    print(no3, " is greater than ", no1)

# Approach 2 - using max() function
print("Greatest of the three numbers is ", max(no1,no2,no3))