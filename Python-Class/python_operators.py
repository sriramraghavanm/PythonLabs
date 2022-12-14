# Numerical operators in Python

# + for addition
# - for substraction
# * for multiplication
# / for float division
# // for integer division
# ** for power calculation
# % for Modulus

x = 5
y = 3

print("Addition of x + y = ", x + y)
print("Substraction of x - y = ", x - y)
print("Multiplication of x * y = ", x * y)
print("Float Division of x / y = ", x / y)
print("Integer Division of x // y = ", x // y)
print("Modulus of x % y = ", x % y)
print("Power of y on x i.e. x ** y = ", x ** y)

# some operations on string
str_data = "raghavan"
empty_str = ''

# concat operation for string
full_name = str_data + " " + "mohan"
print("Full name = ", full_name)

# Can we use '-' as well? It will not work.
# minus_str = "raghavan" - "mohan"
# print("Minus str = ", minus_str)

# multiply_str = "raghavan" * "mohan"
# print("Multiply str = ", multiply_str)

# power_str = "raghavan" ** "mohan"
# print("Power str = ", power_str)

# power_str = "raghavan" ** 3
# print("Power str = ", power_str)

multiply_numeric_str = "raghavan" * 3
print("Multiply numeric str = ", multiply_numeric_str)

# Assignment operators
# =, x = 5
# +=, x += 5 -> x = x + 5
# -=, x -= 5 -> x = x - 5
# *=, x *= 5 -> x = x * 5
# /=, x /= 5 -> x = x / 5
# //=, x //= 5 -> x = x // 5
# %=, x %= 5 -> x = x % 5

# Comparision operators - we compare operand values
# == , Equals to condition, x == y
# != , Not equals to condition, x != y
# >  , Greater than condition, x > y
# <  , Less than condition, x < y
# >= , Greater than and equals to condition, x >= y
# <= , Less than and equals to condition, x <= y

a = 10
b = 5
print("Result of a == b", a == b)
print("Result of a != b", a != b)
print("Result of a > b", a > b)
print("Result of a < b", a < b)
print("Result of a >= b", a >= b)
print("Result of a <= b", a <= b)

# Logical operators in Python (logical check will happen for expression result)
# and - returns True if both the statements are True
# or - returns True if one of the statements is True
# not - reverses the result, returns False if the result is True

m = 10
n = 8
print("m > 10 and n < 10 Result ", m > 10 and n < 10) # False and True - False
print("m > 20 or n < 10 Result ", m > 20 or n < 10) # False or True - True
print("not(m > 20 and n < 10) Result ", not(m > 20 and n < 10)) # not(False and True) - not(False) - True
