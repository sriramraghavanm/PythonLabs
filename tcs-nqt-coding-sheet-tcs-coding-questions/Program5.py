# Check if a number is Armstrong Number or not
# Problem Statement: Given a number, check if it is Armstrong Number or Not.

# Example 1:
# Input:153 
# Output: Yes, it is an Armstrong Number
# Explanation: 1^3 + 5^3 + 3^3 = 153

# Input:170 
# Output: No, it is not an Armstrong Number
# Explanation: 1^3 + 7^3 + 0^3 != 170

# Armstrong Numbers are the numbers having the sum of digits raised to power no. of digits is equal to a given number. Examples- 0, 1, 153, 370, 371, 407, and 1634 are some of the Armstrong Numbers.

no = int(input("Enter a number "))

num = no
sumOfDigitsRaisedToPower = 0
remainder = 0

# This method will give the number of digits for the entered number
def getNoOfDigits(no):
    noOfDigits = 0
    while no != 0:
        remainder = int(no % 10)
        no = int(no / 10)
        noOfDigits = noOfDigits + 1
    return noOfDigits
    
noOfDigits = getNoOfDigits(no)
    
print("Number of digits of the number ",num," is ",noOfDigits)

# This method will raise an individual digit to the power and return the calculated value
def raiseDigitsToPower(digit,power):
    digitRaisedToPower = 1
    for i in range(power):
        digitRaisedToPower = digitRaisedToPower * digit
    return digitRaisedToPower

while num!= 0:
    remainder = int(num % 10)
    num = int(num / 10)
    # get individual digits from the number and pass it as parameter to raiseDigitsToPower method
    sumOfDigitsRaisedToPower = sumOfDigitsRaisedToPower + raiseDigitsToPower(remainder,noOfDigits)
    
if sumOfDigitsRaisedToPower == no:
    print(no, " is an Amstrong number")
else:
    print(no, " is not an Amstrong number")