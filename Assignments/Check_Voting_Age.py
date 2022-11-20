# Code to accept the age of a person as an input. 
# If age >= 18 display "I can vote" and if age is < 18 display "I can't vote".

ageStr = input("Enter person's age - ");
# ageStr is String value, age is int value
age = int(ageStr);

if(age >= 18):
    print("I can vote");
else:
    print("I can't vote");