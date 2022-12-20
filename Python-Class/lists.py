# Declare empty list
L1 = []
# This will return the type of L1
print(type(L1))

# Insert values in the list L1
L1.append(5)
L1.append(7)
L1.append(8)

print(L1)

# Create a list of 100 numbers starting from 1 to 100
int_list = []
print("Initial length of int_list list = ",len(int_list))
for num in range(1,101):
    int_list.append(num)
print(int_list)

# How to calculate the length of a list?
length_of_list = len(int_list)
print("Length of int_list list = ",length_of_list)

# How to check if two lists are equal to each other?
list1 = [1,"Raghavan",20,"Hi"]
list2 = [1,"Raghavan",20,"Hi"]
print("Lists are equal ?? ", list1 == list2)
