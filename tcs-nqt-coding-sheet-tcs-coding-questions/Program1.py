# Check if a number is Palindrome or Not
# Problem Statement:  Given a number check if it is a palindrome.

# Example 1:
# Input: N = 123
# Output: Not Palindrome Number
# Explanation: 123 read backwards is 321.Since these are two different numbers 123 is not a palindrome.

# Example 2:
# Input: N =  121 
# Output: Palindrome Number
# Explanation: 121 read backwards as 121.Since these are two same numbers 121 is a palindrome.

number = int(input("Enter a number - "))
rev = 0
remainder = 0

if number <= 0:    
    print("Please enter a number greater than 0")
else:
    temp = number
    while temp != 0:
        remainder = int(temp % 10)
        temp = int(temp / 10)
        rev = (rev * 10) + remainder
    print("Reverse of ",number," is ",rev)

    # check if reverse is equal to the actual number

    if rev == number:
        print(number, " is a palindrome number")
    else:
        print(number, " is not a palindrome number")