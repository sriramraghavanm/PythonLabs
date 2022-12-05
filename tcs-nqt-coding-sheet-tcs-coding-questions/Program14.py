# Check if given year is a leap year or not
# Problem Statement: Check if the given year is a leap year or not.

# Example 1:
# Input: 1996
# Output: Yes
# Explanation: Since 1996 is a leap year answer is “Yes”.

# Example 2:
# Input: 2000
# Output: Yes
# Explanation: Since 2000 is a leap year answer is “Yes”.

year = int(input("Enter a year "))

if year == 0:
    print("Year cannot be 0")
elif year % 4 == 0 and year % 100 != 0:
    print(year," is a leap year")
elif year % 400 == 0:
    print(year," is a leap year")
else:
    print(year," is not a leap year")