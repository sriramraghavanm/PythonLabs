# Calculate the Area of the Circle
# Problem Statement: Given the radius of the circle, calculate the area of the circle.

radius = int(input("Enter the radius of the circle - "))
pi = 3.14

# Area of the Circle is πr2
area = float(pi * radius * radius)
print("Area of the circle with radius ",radius," is ", area)