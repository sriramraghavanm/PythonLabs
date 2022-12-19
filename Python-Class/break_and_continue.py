# Example for break statement usage

int_list = [1,5,7,8,19,13,17,3]

# Find the even value in the above given list
print("For loop with break statement -")
for num in int_list:
    print("Current element of the list is ",num)
    if num % 2 == 0:
        print("Even number in the list is ",num)
        break
    
# What if break statement is removed
# for num in int_list:
#     print("Current element of the list is ",num)
#     if num % 2 == 0:
#         print("Even number in the list is ",num)

# Above example using while loop

counter = 0

# len() is a in-built function that returns the length of the list
print("While loop with break statement -")
while counter < len(int_list):
    print("Current element of the list is ",int_list[counter])
    if int_list[counter] % 2 == 0:
        print("Even number in the list is ",int_list[counter])
        break
    counter = counter + 1
    
# Example for continue statement usage

# Print the numbers from the for loop and start them from value 1
# but print values in the terminal only if the number is greater than 10

print("For loop with continue statement -")
for num in int_list:
    # print("Current element of the list is ",num)
    if not(num > 10): # Can also use num < 10 - continue
        continue
    print(num)
    
print("While loop with continue statement -")
counter = 0
while counter < len(int_list) - 1:
    counter = counter + 1
    if int_list[counter] < 10:
        continue
    print(int_list[counter])
