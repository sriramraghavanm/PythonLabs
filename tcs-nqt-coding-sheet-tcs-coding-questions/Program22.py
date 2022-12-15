# Check if a number is a Strong Number or not
# Problem Statement: Given an integer Print “YES” if it is a strong number else print “NO”.

# Note : 

# When the sum of factorial of individual digits of a number is equal to the original number the number is called a strong number. 
# Strong number is also known as Krishnamurthi number/Peterson Number.

# Examples 1:
# Input: N = 145
# Output: Yes
# Explanation: 1! + 4! + 5! = 145. Hence 145 is a strong number. 

# Example 2:
# Input:  26
# Output: No
# Explanation: 2! + 6! = 722. Hence 26 is not a strong number.

no = int(input("Enter a number "))

def isStrongNumber(no):
    actualNo = no
    sum = 0 # this will store the sum of factorial of individual digits
    while no != 0:
        remainder = int(no % 10)
        no = int(no / 10)
        sum = sum + getFactorial(remainder)
    print("Sum of factorial of individual digits ",sum)
    
    if sum == actualNo:
        return True
    else:
        return False
    
def getFactorial(no):
    factorial = 1
    while no != 0:
        factorial = factorial * no
        no = no - 1
    print("factorial ",factorial)
    return factorial
    
if isStrongNumber(no):
    print(no, " is a Strong number")
else:
    print(no, " is not a Strong number")