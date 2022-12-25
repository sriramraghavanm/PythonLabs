# Dictionary in Python

dict1 = {}
print("Type of dict1 = ",type(dict1))

# How to insert values in a dictionary
dict2 = {}
# 'name' is the key and 'Raghavan' is the value mapped against it
dict2['name'] = 'Raghavan'
# 'age' is the key and 38 is the value mapped against it
dict2['age'] = 38
# 'skills' is the key and value is a list here containing "Java" and "Python"
dict2['skills'] = ['Python','Java']
dict2['states_visited'] = ('UP','Maharashtra','Madhya Pradesh')
dict2[45] = 'Random Key'
# Another dictionary
# dict3 = {'color':'Black','nationality':'Indian'}
# Nested dictionary example
# dict2['other_details'] = dict3
dict2['other_details'] = {'color':'Black','nationality':'Indian'}

print("Contents of dict2 = ",dict2)

# Check the length of a dictionary. Returns number of keys we have created in our dictionary
print("Length of the dictionary dict2 = ", len(dict2))

# How to access value of a particular key?
print(dict2['age'])
print(dict2['skills'][1]) # Will print Java
# Accessing dictionary within a dictionary i.e. nested dictionary
print(dict2['other_details']['color'])
print(dict2['other_details']['nationality'])

# How to update value on a particular key?
# updating the age
dict2['age'] = 36
print(dict2['age'])
print("Contents of dict2 = ",dict2)

# How to get distinct keys from a dictionary
total_keys = dict2.keys()
# this will return dict_keys which is not an actual list
print("Distinct keys from dict2 = ",total_keys)
# to get actual list use typecasting
print("List of keys from dict2 = ",list(total_keys))

# How to get distinct values from a dictionary
total_values = dict2.values()
# this will return dict_values which is not an actual list
print("Values from dict2 = ",total_values)
# to get actual list use typecasting
print("List of values from dict2 = ",list(total_values))

# How to iterate on the dictionary?
for k,v in dict2.items():
    print("Key is",k,"and value is",v)
    
# Compare two dictionaries
dict3 = {'a':1,'b':2,'c':3}
dict4 = {'b':2,'c':3,'a':1}
print("Is dict3 == dict4 ?? = ",dict3 == dict4)

dict5 = {'a':1,'b':2,'c':3}
dict6 = {'b':2,'c':3,'a':5}
# Keys are same in both the dicts, but values are different
print("Is dict5 == dict6 ?? = ",dict5 == dict6)

# How to delete specific key-value pair from the dictionary
print("Before delete = ",dict2)
del dict2['age']
del dict2[45]
print("After delete = ",dict2)

# How to check if a particular key exists in dictionary or not ?
keys_in_dict = list(dict2.keys())
if 'other_details' in keys_in_dict:
    print("True")
else:
    print("False")
