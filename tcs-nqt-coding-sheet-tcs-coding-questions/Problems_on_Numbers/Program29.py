# Find the sum of numbers in the given range
# Problem Statement: Find the sum of numbers in the given range.

startNo = int(input("Enter starting number - "))
endNo = int(input("Enter ending number - "))

sum = 0
temp = startNo

print("Starting number is ", startNo)

while temp <= endNo:
    sum = sum + temp
    temp = temp + 1
    if temp < endNo:
        print(temp)

print("Ending number is ", endNo)

print("Using While Loop: Sum of all the numbers between ", startNo, " and ", endNo, " is ", sum)

# Approach 2 - Using For Loop
sum = 0

for i in range(endNo + 1):
    if i >= startNo:
        print(i)
        sum = sum + i
print("Using For Loop: Sum of all the numbers between ", startNo, " and ", endNo, " is ", sum)