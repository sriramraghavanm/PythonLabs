# Check if the given number is Harshad(Or Niven) Number
# Problem Statement: Check if the number is a Harshad(or Niven) number or not.

# Example 1:
# Input: 378
# Output: Yes it is a Harshad number.
# Explanation: 3+7+8=18. 378 is divisible by 18. Therefore 378 is a harshad number.

# Example 2:
# Input: 379
# Output: No it is not a Harshad number.
# Explanation: 3+7+9=19. 379 is not divisible by 19. Therefore 379 is a harshad number.

number = int(input("Enter a number - "))
actualNumber = number

sum = 0
remainder = 0

if actualNumber == 0 or actualNumber < 10:
    print("Number should be greater than 10")
else:
    while number != 0:
        remainder = int(number % 10)
        number = int(number / 10)
        sum = sum + remainder

    if actualNumber % sum == 0:
        print("Yes it is a Harshad number")
    else:
        print("No it is not a Harshad number")