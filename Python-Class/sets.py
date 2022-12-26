# Sets in Python

set1 = set() # this will create an empty set object and assign it to set1
print(type(set1))

# A list with duplicate elements
list1 = [1,2,3,4,1,2,3,4,5,6,7,8,1]
# Assigning list as a parameter to set()
set2 = set(list1)
print("Elements of the list list1 = ",list1)
print("Elements of the set set2 = ",set2)

set3 = {1,2,3,4,5,2,1,4} # this will not throw an error, however at runtime duplicate elements will be removed  
print("Elements of set3 = ",set3)
print("Length of set3 = ",len(set3)) # Only distinct elements will be counted here

# Dictionary
set4 = {}
print("Elements of set4 = ",set4)
print("Type of set4 = ",type(set4))

# How we can iterate elements in the set
for num in set2:
    print(num)

# converting output of set into a list
set5 = list(set(list1))
print("Contents of set5 = ",set5)
print("Type of set5 = ",type(set5))
print("Printing list contents in reverse = ")
print(set5[-1])
print(set5[-2])
print(set5[-3])
print(set5[-4])
print(set5[-5])
print(set5[-6])
print(set5[-7])
print(set5[-8])

print("Printing list contents using for loop = ")
for num in set5:
    print(num)
    
print("Printing list contents using while loop = ")
counter = 0
while counter < len(set5):
    print(set5[counter])
    counter += 1
    
# How to insert elements in the set
set6 = set()
set6.add(1)
set6.add(1)
set6.add(2)
set6.add(5)
set6.add(2)
set6.add(1)
set6.add(2)

print("Contents of set6 = ",set6)

# Use of update() method
tmp = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,6]
# when update() method is used, duplicate elements will be removed and added to the set
# set6 already has 1,2 and 5. 3,4 and 6 are new and hence only 3,4 and 6 will get added to set6
set6.update(tmp)
print("Contents of set6 after update = ",set6)

# Set operations
set_a = {1,2,3,4,5,6}
set_b = {3,6,8,9,10}

# Union operator
# Will combine both the sets, removing duplicate elements
print("Union of set_a and set_b = ",set_a.union(set_b))
print("Union of set_a and set_b = ",set_a | set_b)

# Intersection operator
# Getting common values
print("Intersection of set_a and set_b = ",set_a.intersection(set_b))
print("Intersection of set_a and set_b = ",set_a & set_b)

# Difference in Sets
# Set A - Set B
# set_a - set_b means all the elements from set_a except those values which are also present in set_b
print("set_a - set_b = ",set_a - set_b)
# Set B - Set A
# set_b - set_a means all the elements from set_b except those values which are also present in set_a
print("set_b - set_a = ",set_b - set_a)

# Comparision in Sets
set_x = {1,2,3,4,5}
set_y = {1,2,3,5,4,5,1}
print("set_x == set_y is",set_x == set_y)

set_m = {1,2,3,4,5,6} # Internally it is {1,2,3,4,5,6}
set_n = {1,2,3,5,4,5,1} # {1,2,3,4,5}
print("set_m == set_n is",set_m == set_n)
