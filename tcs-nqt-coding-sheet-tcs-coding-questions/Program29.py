# Find the sum of numbers in the given range
# Problem Statement: Find the sum of numbers in the given range.

# Example 1:
# Input: l=2, r=7
# Output: 27
# Explanation: 2+3+4+5+6+7=27. Therefore 27 is the answer.

# Example 2:
# Input: l=5, r=9
# Output: 35
# Explanation: 5+6+7+8+9=35. Therefore 35 is the answer.

startNo = int(input("Enter starting number - "))
endNo = int(input("Enter ending number - "))

sum = 0

if startNo == endNo:
    print("startNo and endNo cannot be same")
elif startNo > endNo:
    print("startNo cannot be greater than endNo")
else:
    # Approach 1 - Using For Loop
    for no in range(startNo,endNo + 1):
        sum = sum + no
    print("Using For Loop: Sum of all the numbers between ", startNo, " and ", endNo, " is ", sum)
    
    # Approach 2 - Using While Loop
    sum = 0
    temp = startNo
    while temp < endNo + 1:
        sum = sum + temp
        temp = temp + 1
    print("Using While Loop: Sum of all the numbers between ", startNo, " and ", endNo, " is ", sum)