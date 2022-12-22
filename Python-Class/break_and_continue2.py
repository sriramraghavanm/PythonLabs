# Example to demonstrate usage of break and continue

list1 = [1,2,3,4,5,6,7,8,9]

# Print all the values from the list except 4
# When 4 is encountered, do nothing just skip it
print("continue usage example -")
for index in list1:
    if index == 4:
        continue
    print(index)
    
# Once 4 is encountered break the loop and stop execution
print("break usage example -")
for index in list1:
    print(index)
    if index == 4:
        break
