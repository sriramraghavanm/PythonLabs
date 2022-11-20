# Program to check if a number is even or odd

number = input("Enter a number - ");

# By default input() always accept 'String' values
# type() will give datatype
datatype = type(number);
print("Data type is ", datatype);

# int() is used to typecast into integer
if int(number) % 2 == 0:
    print("Number is even");
else:
    print("Number is odd");