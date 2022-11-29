# Sum of first N Natural Numbers
# Problem statement: Given a number ‘N’, find out the sum of the first N natural numbers.

n = int(input("Enter a number - "))
#print("Number entered is ", n)

sum = 0

for i in range(n + 1):
    sum = sum + i

print("Sum of first ",n," natural numbers is ",sum)

# Approach 2 - Second approach using the formula, n = n(n+1)/2

sum = int(n * (n + 1)/2)

print("Using Formula  method : Sum of first ",n," natural numbers is ",sum)