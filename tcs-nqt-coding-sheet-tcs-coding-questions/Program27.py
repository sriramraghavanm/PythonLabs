# Check if the number is an abundant number or not
# Problem Statement: Check if the number is an abundant number or not.

# Example 1:
# Input: 18
# Output: Abundant Number
# Explanation: Divisors of 18 are 1,2,3,6,9. 1+2+3+6+9=21, Since 21 is greater than 18, 18 is an abundant number.

# Example 2:
# Input: 21
# Output: Not Abundant Number
# Explanation:Divisors of 21 are 1,3,7. 1+3+7=11, Since 11 is smaller than 21, 11 is not an abundant number.

no = int(input("Enter a number "))

def isAbundantNumber(no):
    sumOfDivisors = 0
    for i in range(no):
        i = i + 1
        if no % i == 0 and i < no:
            sumOfDivisors = sumOfDivisors + i
    print("sumOfDivisors ",sumOfDivisors)
    
    if sumOfDivisors > no:
        return True
    else:
        return False
        
if isAbundantNumber(no):
    print(no, " is an abundant number")
else:
    print(no, " is not an abundant number")