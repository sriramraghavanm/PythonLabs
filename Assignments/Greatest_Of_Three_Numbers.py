# Code to take 3 numbers as an input from the user and display the greatest no as output.

# These statements will accept the input from user and also typecast it into integer
number1 = int(input("Enter the first number - "));
number2 = int(input("Enter the second number - "));
number3 = int(input("Enter the third number - "));

# Logic to check greatest of three numbers
if((number1 > number2) & (number1 > number3)):
    print("Greatest number is - ", number1);
elif((number2 > number3) & (number2 > number1)):
    print("Greatest number is - ", number2);
else:
    print("Greatest number is - ", number3);