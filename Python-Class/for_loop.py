# Write a code to print numbers from 1 to 10

# range(1,11) creates a list i.e. [1,2,3,4,5,6,7,8,9,10]
# for num in range(1,11): 
#     print(num)
    
# Write a code to print numbers from 1 to 10 using 2 steps as increment
#  OR
# Example to print odd numbers starting from value 1
# for num in range(1,11,2):
#     print(num)
    
# Write a code to print numbers from 10 to 1 in reverse
for num in range(10,0,-1):
    print(num)
    
# Write a program to calculate the sum of given list elements using the for loop
# output = 25
int_list = [4,8,-2,10,5]
list_sum = 0
for num in int_list:
    list_sum = list_sum + num
print("output = ",list_sum)
