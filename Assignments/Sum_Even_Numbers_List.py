# Code that displays the sum of all the even numbers from the given list

numberList = [12, 75, 150, 180, 145, 525, 50];
sumOfEvenNumbers = 0;

# for loop to traverse the list
# for i in numberList:
#    print(i);

# Logic to check traverse the list, check if particular number is even and then add even numbers
for number in numberList:
    if(number % 2 == 0):
        sumOfEvenNumbers = sumOfEvenNumbers + number;

print("Sum of even numbers from the list is - ", sumOfEvenNumbers);