# Code to take 3 numbers as an input from the user and display the greatest no as output.

# These statements will accept the input from user and also typecast it into integer
no1 = int(input("Enter the first number - "));
no2 = int(input("Enter the second number - "));
no3 = int(input("Enter the third number - "));

# Logic to check greatest of three numbers
if((no1 > no2) & (no1 > no3)):
    print("Greatest number is - ", no1);
elif((no2 > no3) & (no2 > no1)):
    print("Greatest number is - ", no2);
else:
    print("Greatest number is - ", no3);