# Find all Palindrome Numbers in a given range
# Problem Statement: Given a range of numbers, find all the palindrome numbers in the range.

# Example 1:
# Input: min = 10 , max = 50
# Output: 11 22 33 44 
# Explanation: 11, 22, 33, 44 will remain the same when they read from forward or backward.

# Example2:
# Input: min = 100 , max = 150
# Output: 101 111 121 131 141 
# Explanation: 11, 22, 33, 44 will remain the same when they read from forward or backward.

min = int(input("Enter min "))
max = int(input("Enter max "))

print("Palindrome's between ",min," and ",max," - ")

# This method will check if a number is a palindrome or not and accordingly return True or False
def isPalindrome(no):
    actualNo = no
    remainder = 0
    rev = 0
    
    while no!= 0:
        remainder = int(no % 10)
        no = int(no / 10)
        rev = rev * 10 + remainder

    if rev == actualNo:
        return True
    else:
        return False
    
if min == max:
    print("min and max cannot be same")
elif min > max:
    print("min cannot be greater than max")
else:
    while min <= max:
        if isPalindrome(min) == True:
            print(min, " is a palindrome")
        # else:
        #    print(min, " is not a palindrome")
        min = min + 1