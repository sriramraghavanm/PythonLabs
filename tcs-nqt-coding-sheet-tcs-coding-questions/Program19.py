# Calculate the Power of a Number : Binary Exponentiation
# Problem Statement: Find the Power of a number.

# Example 1:
# Input: N = 5, k=3
# Output: 125
# Explanation: Since 5*5*5 is 125.

# Example 2:
# Input: n=2 k=4
# Output: 16
# Explanation: Since 2*2*2*2 is 16

number = int(input("Enter a number - "))
power = int(input("Enter the power you want to raise to - "))

ans = 1

# Approach 1 - Using power library function

print("Using library function pow() : ", number, " raised to the power of ", power, " is ", pow(number,power))

# Approach 2 - Using for loop

for i in range(power):
    ans = ans * number

print("Using for loop : ",number, " raised to the power of ", power, " is ", ans)

# Approach 3 - Using while loop

ans = 1
temp = power

while temp > 0:
    ans = ans * number
    temp = temp - 1

print("Using while loop : ",number, " raised to the power of ", power, " is ", ans)