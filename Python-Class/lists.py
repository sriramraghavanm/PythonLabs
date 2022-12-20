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

# If sequence of elements are changed will the lists be equal?
list1 = [1,"Raghavan",20,"Hi"]
list2 = [1,"Raghavan","Hi",20]
print("Lists are equal ?? ", list1 == list2)

# Adding two lists or "concatenating" two lists
list3 = [1,2,3,4,5]
list4 = [80,90,100,110]
result = list3 + list4
print(result)

# How to access list values
# Print all the elements of the given list
list5 = [10,15,20,25,30,35]
# print(list5) - this cannot be used if we want to print individual elements in the terminal
for num in list5:
    print(num)
    
# Print 3rd element from the given list - [10,15,20,25,30,35]
# List index will start from 0
print("3rd element from the given list = ",list5[2])

print(list5[0])
print(list5[1])
print(list5[2])
print(list5[3])
print(list5[4])
print(list5[5])

# What will happen when this is executed ?
# It will throw IndexError - list index out of range
# print(list5[100])

# How to update the value of list index item ?
# Update "Raghavan" to "Rahul"
list6 = [1,"Raghavan",1000]
print("Before update = ",list6)
list6[1] = "Rahul"
print("After update = ",list6)

# How to print list elements using length ?
for index in range(0,len(list6)):
    print(list6[index])
    
list7 = [1,2,50,"Raghavan",[6,6,6],"Rahul"]
print("Length of list7 list = ",len(list7))

# Difference between append() and extend()
list8 = [20,30,40]
list9 = ["hi","hello","bye"]
list8.append(list9)
print("Output of Append = ",list8)
print("Length after Append = ",len(list8))

list10 = [20,30,40]
list11 = ["hi","hello","bye"]
list10.extend(list11)
print("Output of Extend = ",list10)
print("Length after Extend = ",len(list10))

# List slicing
# End index is always exclusive
list12 = [20,30,40,50,60,80,90]
# syntax -> list_name[start : end]
print(list12[0 : ])
# Now what will be the output ?
print(list12[3 : ])
# Now what will be the output ?
print(list12[ : ])
print(list12[0 : 4])
# Print values from 40 to 80
print(list12[2 : 6])
print(list12[0 : : 2]) # 3rd value is for step increment

# How to print the last value of the list - [20,30,40,50,60,80,90]
print("Last value of the list = ",list12[len(list12) - 1])
# Negative 1 or -1 index means last element of the list
print("Last value of the list = ",list12[- 1])
# How to print the second last value of the list - [20,30,40,50,60,80,90]
print("Second last value of the list = ",list12[- 2])

# Print list in reverse direction
print(list12[-1 : : -1])
