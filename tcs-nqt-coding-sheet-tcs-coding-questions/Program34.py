# Calculate the Area of the Circle
# Problem Statement: Given the radius of the circle, calculate the area of the circle.

# Example 1:
# Input: N = 5
# Output: 78.5
# Explanation: Using formula  πr2 for finding area of circle we get area as 78.5

# Example 2:
# Input: N = 4
# Output: 50.2
# Explanation: Using formula  πr2 for finding area of circle we get area as 50.2

radius = int(input("Enter the radius of the circle - "))

pi = 3.14
area = 0

if radius == 0:
    print("Radius cannot be zero. Enter a non-zero radius")
else:
    # Area of the Circle is πr2
    area = float(pi * radius * radius)
    print("Area of the circle with radius", radius, " is ", area)