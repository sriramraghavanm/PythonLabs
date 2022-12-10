# Find Sum of AP Series
# Problem Statement: Given an A.P. Series, we need to find the sum of the Series.

#   a = first term of A.P.
#   d= common Difference of A.P.
#   n= Number of Terms in  A.P.

#   Example 1:
#   Input:
#   n=4
#   a=2
#   d=2
#   Output: 20
#   Explanation: 2+4+6+8 = 20

#   Input:
#   n=8
#   a=2
#   d=5
#   Output: 124
#   Explanation: -2 +3 + 8 + 13 + 18 + 23 + 28 + 33 = 124

#   A.P. is the series of terms having the first term as a and d, common difference. Every next term in the A.P. is greater than the previous term by d units.

#   Example – 

#   -2, 3 , 8 , 13 , 18 , 23 , 28 , 33

#   First term , a = – 2
#   Common Difference , d=5
#   number of terms in the AP , an=33

a = float(input("Enter the first term in the AP "))
d = float(input("Enter the common difference "))
n = int(input("Enter the number of terms in the AP "))

sumOfAP = 0

# Approach 1 - using formula sn = (n/2)(2a + (n - 1)d)
sumOfAP = float((n / 2) * (2 * a + (n - 1) * d))
print("Sum of the AP Series ",sumOfAP)

# Approach 2 - using while loop
while n < 0:
    sumOfAP = sumOfAP + a
    a = a + d
    n = n - 1
print("Using while loop: Sum of the AP Series ",sumOfAP)

# Approach 3 - using for loop
sumOfAP = 0
for i in range(n):
    sumOfAP = sumOfAP + a
    a = a + d
    
print("Using for loop: Sum of the AP Series ",sumOfAP)