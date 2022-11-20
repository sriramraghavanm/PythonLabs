# Write a program to display only those numbers from a list that satisfy the following conditions
# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop

numberList = [12, 75, 150, 180, 145, 525, 50];

# for loop will iterate through the list
for number in numberList:
    # if the number is greater than 500 break the loop
    if(number > 500):
        break;
    # if the number is greater than 150 then skip to next element
    elif(number > 150):
        continue;
    # if the number is less than 150 and divisible by 5, print the number
    elif (number % 5 == 0):
        print(number);