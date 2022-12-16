# Declare and assign variables in Python

int_var = 10
float_var = 18.25
string_var = 'ineuron batch2' # can use "ineuron batch2" also
bool_var = True # if we want to assign false then it should be like False

# Function in Python for output
# Function does what? They might or might not accept some parameters
print("Hello World !!!") 

# Print variable values in Python
print("Value of int_var = ",int_var," - Result Done !!!")
print("Value of float_var = ",float_var," - Result Done !!!")
print("Value of string_var = ",string_var," - Result Done !!!")
print("Value of bool_var = ",bool_var," - Result Done !!!")

# How to check the data type of any variable in Python ?
# we can use type() function. It is in-built function
print("Type of int_var ? ",type(int_var))
print("Type of float_var ? ",type(float_var))
print("Type of string_var ? ",type(string_var))
print("Type of bool_var ? ",type(bool_var))

# How to do the type casting in Python ?
# float(), str(), bool(), int()
int_var = int_var + 10 # int_var = int_var + 10 will become int_var = 10 + 10 i.e. int_var = 20
casted_int_var = float(int_var)
casted_float_var = int(float_var)

print("Int to Float Typecasting for int_var ",casted_int_var)
print("Float to Int Typecasting for float_var ",casted_float_var)

numeric_str  = "123"
# numeric_str = numeric_str + 50 # is this valid?
# print("Value of numeric_str ",numeric_str)

numeric_str = int(numeric_str) + 50 # this will get evaluated as int("123") + 50 i.e. 123 + 50 = 173
print("Value of numeric_str ",numeric_str)

# How to take inputs in Python ?
# we can use input() function
# name = input()
# age = input()
# print("User's name = ",name)
# print("User's age = ",age)

# Another way to take user input with custom message
# name = input("Enter a value for name ")
# age = input("Enter a value for age ")
# print("User's name = ",name)
# print("User's age = ",age)

# Convert type of data during input
name = input("Enter a value for name ")
age = int(input("Enter a value for age "))
print("User's name = ",name)
print("User's age = ",age)

print("Type of name = ",type(name))
print("Type of age = ",type(age))
