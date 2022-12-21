# Create a String in Python

str1 = "Raghavan"
print(str1)

str2 = "Raghavan's"
print(str2)

str3 = 'He is a "Good" guy'
print(str3)

# Use len function
print("Length of the string = ",len(str3))

# How to write multiline String
str4 = '''My name is Raghavan.
I know DevOps and Cloud.
I am learning Python now.
I want to be a Senior Data Engineer.'''
print(str4)

# String concatenation
str5 = "Raghavan"
str6 = "Sriram"
print("String concatenation ",str5 + str6)

# String comparision
str7 = "Raghavan"
str8 = "Raghavan"
print("String concatenation ",str7 == str8)

# How to print each character from the String
# for char in str7:
#     print(char)

print(str7[0])
print(str7[1])
print(str7[2])
print(str7[3])
print(str7[4])
print(str7[5])
print(str7[6])
print(str7[7])

# Update the 4th character in the string by M
# str8 = "Raghavan"
# str8[3] = 'M'
# print(str8)

# Convert string into lower case
print(str8.lower())

# Convert string into upper case
print(str8.upper())

# Other functionalities will be same as List like Slicing
