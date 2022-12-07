# Program to swap two numbers
# Example a = 10, b = 5; output should be a = 5 and b = 10

no1 = int(input("Enter no1 "))
no2 = int(input("Enter no2 "))

# Approach 1: Swapping 2 numbers using a temp variable

print("Before swapping no1 = ",no1," and no2 = ",no2)

if no1 == no2:
    print("Both the numbers are same")
else:
    temp = no1
    no1 = no2
    no2 = temp
    print("After swapping no1 = ",no1," and no2 = ",no2)
    
# Approach 2: Swapping 2 numbers without using a third or temp variable or swapping only using two variables

    print("Now no1 = ",no1," and no2 = ",no2)
    no1 = no1 + no2
    no2 = no1 - no2
    no1 = no1 - no2
    print("Using Approach 2: no1 = ",no1," and no2 = ",no2)