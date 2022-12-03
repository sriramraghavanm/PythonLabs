# Check whether a number is positive or negative
# Problem statement: Given a number n check whether it’s positive or negative.

# Example 1:
# Input: n=5
# Output: Positive

# Example2:
# Input: n=-6
# Output: Negative

no = int(input("Enter a number - "))

if no == 0:
    print("The number zero is neither positive nor negative.")
elif no > 0:
    print("Number is positive.")
else:
    print("Number is negative.")